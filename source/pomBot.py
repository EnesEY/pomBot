from config.config import Config
from datetime import datetime
import threading
import time
from dadjokes import Dadjoke
from source.urlFactory import URLFactory
from requests import get, post, put
from logging import Logger
import json
from typing import List
from dateutil.parser import parse


class PomBot:
    config: Config

    def __init__(self, config: Config, logger: Logger):
        self._cycle_thread: threading.Thread = None
        self.config = config
        self.logger = logger

    def start_cycle(self):
        self._cycle_thread = threading.Thread(target=self._cycle)
        self.stop = False
        self._cycle_thread.start()

    def stop_cycle(self):
        self.stop = True
        self._cycle_thread.join()

    def _cycle(self):
        self.logger.info("Start PomBot")
        timerConfig = self.config.pomTimeConfig
        while not self.stop:
            current_minute = datetime.now().minute
            end_minute = (timerConfig.pom_start_time + timerConfig.pom_duration) % 60
            self.logger.info(
                f"start_min: {timerConfig.pom_start_time} end_min: {end_minute} current_min: {current_minute}"
            )
            if current_minute == timerConfig.pom_start_time:
                self._execute_pom_start_process()
            elif current_minute == end_minute:
                self._execute_pom_end_process()
            time.sleep(60 * timerConfig.pom_break_duration)

    def _execute_pom_start_process(self):
        if self.config.messagesConfig.sendMessagesJobActivated == True:
            self.send_message(self.config.messagesConfig.pomStartMessage)
            last_sent_message_id = self.get_last_message_id_for_payload(
                self.config.messagesConfig.pomStartMessage
            )
        if self.config.reactEmojisConfig.reactEmojisJobActivated:
            self.react_with_list_of_emojis(
                last_sent_message_id, self.config.reactEmojisConfig.pomStartReactEmojis
            )
        if self.config.markOwnMessagesUnreadConfig.markOwnMessageUnreadActivated:
            self.mark_own_message_unread(last_sent_message_id)  ###sssss
        if self.config.dadJokesConfig.dadJokeJobActivated:
            dadjoke = Dadjoke()
            self.send_message(f"|| {dadjoke.joke} ||")

    def _execute_pom_end_process(self):
        if self.config.messagesConfig.sendMessagesJobActivated:
            self.send_message(self.config.messagesConfig.pomEndMessage)
            last_sent_message_id = self.get_last_message_id_for_payload(
                self.config.messagesConfig.pomEndMessage
            )
        if self.config.reactEmojisConfig.reactEmojisJobActivated:
            self.react_with_list_of_emojis(
                last_sent_message_id, self.config.reactEmojisConfig.pomEndReactEmojis
            )
        if self.config.markOwnMessagesUnreadConfig.markOwnMessageUnreadActivated:
            self.mark_own_message_unread(last_sent_message_id)
        if self.config.afkCheckConfig.checkAfksJobActivated:
            self.check_afks()
        if self.config.dadJokesConfig.dadJokeJobActivated:
            dadjoke = Dadjoke()
            self.send_message(f"|| {dadjoke.joke} ||")

    def send_message(self, message: str):
        try:
            payload = {"content": message}
            header = {"authorization": self.config.secret_token}
            channel_url = URLFactory.create_message_url(self.config.channel_id)
            post(channel_url, data=payload, headers=header)
            self.logger.info(
                f"Message: {message} sent successfully to channel_id: {self.config.channel_id}"
            )
            time.sleep(1)
        except Exception as ex:
            self.logger.error(
                f"Message {message} could not be sent to channel_id: {self.config.channel_id} Exception: {type(ex).__name__}"
            )

    # searches for the given message in the last 100 messages and returns the message_id of that message
    # if multiple messages with the same content are found in the last 100 messages the last message_id is returned
    def get_last_message_id_for_payload(self, message: str) -> int:
        limit = 100  # max. limit for discord api
        channel_url = URLFactory.create_message_url(self.config.channel_id)
        header = {"authorization": self.config.secret_token}
        payload = {"limit": limit}
        try:
            response = get(channel_url, headers=header, params=payload)
            messages = json.loads(response.text)
            message_ids_for_payload = [
                data["id"] for data in messages if data["content"] == message
            ]
            last_message_id_for_payload = message_ids_for_payload[0]
        except Exception as ex:
            self.logger.error(
                f"Couldn't get messages from channel_id: {self.config.channel_id} Exception: {type(ex).__name__}"
            )
        return last_message_id_for_payload

    def react_with_list_of_emojis(self, message_id: int, emoji_list: List[str]):
        header = {"authorization": self.config.secret_token}
        for emoji_string in emoji_list:
            react_emoji_url = URLFactory.create_react_with_emoji_url(
                self.config.channel_id, message_id, emoji_string
            )
            put(react_emoji_url, headers=header)
            self.logger.info(
                f"Reacted with Emoji {emoji_string} on message_id: {message_id}"
            )
            time.sleep(1)

    def mark_own_message_unread(self, message_id: int):
        payload = json.dumps({"manual": True, "mention_count": 1})
        header = {
            "authorization": self.config.secret_token,
            "Content-Type": "application/json",
        }
        mark_own_message_unread_url = URLFactory.create_mark_own_message_unread_url(
            self.config.channel_id, message_id
        )
        post(mark_own_message_unread_url, data=payload, headers=header)
        self.logger.info(f"message {message_id} was marked unread")

    def get_all_messages_in_time_frame(self, time_frame_in_s: int):
        limit = 100  # max. limit for discord api
        channel_url = URLFactory.create_message_url(self.config.channel_id)
        header = {"authorization": self.config.secret_token}
        payload = {"limit": limit}
        response = get(channel_url, headers=header, params=payload)
        messages = json.loads(response.text)

        if len(messages) < limit:
            current_timestamp = datetime.now().timestamp()
            messages_in_timeframe = [
                data
                for data in messages
                if (current_timestamp - parse(data["timestamp"]).timestamp())
                < time_frame_in_s
            ]
            return messages_in_timeframe

        while (
            datetime.now().timestamp() - parse(messages[-1]["timestamp"]).timestamp()
        ) < time_frame_in_s:
            last_message_id = messages[-1]["id"]
            before_message_url = URLFactory.create_before_message_url(
                self.config.channel_id, last_message_id
            )
            response = get(before_message_url, headers=header)
            json_data = json.loads(response.text)
            messages += json_data
            if len(json_data) < limit:
                break
        current_timestamp = datetime.now().timestamp()
        messages_in_timeframe = [
            data
            for data in messages
            if (current_timestamp - parse(data["timestamp"]).timestamp())
            < time_frame_in_s
        ]
        return messages_in_timeframe

    def get_recipients(self):
        header = {"authorization": self.config.secret_token}
        recipients_url = URLFactory.create_recipients_url(self.config.channel_id)
        response = get(recipients_url, headers=header)
        json_data = json.loads(response.text)
        usernames = [
            d.get("global_name") or d.get("username")
            for d in json_data["recipients"]
            if "username" in d or "global_name" in d
        ]
        return usernames

    # checks which users didn't send messages in time_frame_in_s and sends a warning for those users
    def check_afks(self):
        messages = self.get_all_messages_in_time_frame(
            self.config.afkCheckConfig.maxSecondsOld
        )
        authors = [subdict["author"] for subdict in messages]
        usernames = [
            d.get("global_name") or d.get("username")
            for d in authors
            if "username" in d or "global_name" in d
        ]
        unique_usernames = list(set(usernames))
        recipients = self.get_recipients()
        missing_usernames = list(set(recipients) - set(unique_usernames))
        info_str = ""
        for name in missing_usernames:
            info_str += name + " "
        if info_str != "":
            self.send_message(f"users: {info_str}seem to be afk")
