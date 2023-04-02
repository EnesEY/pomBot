from config.config import Config, PomTimeType
from source.sendMessage import SendMessage
from source.reactWithEmoji import ReactWithEmoji
from source.receiveMessage import ReceiveMessage
from source.markMessageUnread import MarkMessageUnread
from source.checkAfks import CheckAfks
import datetime
import threading
import time


class PomBot:
    channel_string: str
    config: Config
    pomStartMin: int
    pomEndMin: int
    pomDurationInMin: int
    pomBreakTimeInMin: int
    secret_token: str

    def __init__(
        self,
        channel_id: int,
        config: Config,
        pomTimeConfig: PomTimeType,
        secret_token: str,
        pomStartMin=None,
        pomEndMin=None,
        pomDurationInMin=None,
        pomBreakTimeInMin=None,
    ):
        self._cycle_thread: threading.Thread = None
        self.channel_string = self._get_channel_string(channel_id)
        self.pomStartMin = pomStartMin
        self.pomEndMin = pomEndMin
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.config = config
        self.secret_token = secret_token
        self._load_pom_times(pomTimeConfig)

    def _get_channel_string(self, channel_id: int):
        channel_string_start = "https://discord.com/api/v9/channels/"
        channel_string_end = "/messages"
        return channel_string_start + str(channel_id) + channel_string_end

    def _load_pom_times(self, pomTimeConfig: PomTimeType):
        def _closest_minute_in_future(minutes):
            now = datetime.datetime.now().minute
            time_differences = [abs(curr_time - now) for curr_time in minutes]
            min_time_difference = min(time_differences)
            closest_minute = minutes[time_differences.index(min_time_difference)]
            return closest_minute

        if pomTimeConfig == PomTimeType.POM_TIME_TYPE_DEFAULT_25:
            self.pomDurationInMin = 25
            self.pomBreakTimeInMin = 5
            closest_minute = _closest_minute_in_future([0, 25, 30, 55])
            if closest_minute == 0 or closest_minute == 30:
                self.pomStartMin = closest_minute
                self.pomEndMin = 111
            else:
                self.pomStartMin = 111
                self.pomEndMin = closest_minute
        elif pomTimeConfig == PomTimeType.POM_TIME_TYPE_DEFAULT_50:
            self.pomDurationInMin = 50
            self.pomBreakTimeInMin = 10
            closest_minute = _closest_minute_in_future([0, 50])
            if closest_minute == 0:
                self.pomStartMin = closest_minute
                self.pomEndMin = 111
            else:
                self.pomStartMin = 111
                self.pomEndMin = closest_minute
        else:
            print("pom times should be set in pomBot constructor")

    def start_cycle(self):
        self._cycle_thread = threading.Thread(target=self._cycle)
        self.stop = False
        self._cycle_thread.start()

    def stop_cycle(self):
        self.stop = True
        self._cycle_thread.join()

    def _cycle(self):
        print("start cycle for send job")
        while not self.stop:
            if datetime.datetime.now().minute == self.pomEndMin:
                self._execute_end_messages()
                time.sleep(
                    (self.pomBreakTimeInMin * 60) - (datetime.datetime.now().second)
                )
                self.pomStartMin = datetime.datetime.now().minute
                self.pomEndMin = 999
            if datetime.datetime.now().minute == self.pomStartMin:
                self._execute_start_messages()
                time.sleep(
                    (self.pomDurationInMin * 60) - (datetime.datetime.now().second)
                )
                self.pomEndMin = datetime.datetime.now().minute
                self.pomStartMin = 999
            time.sleep(1)

    def _execute_start_messages(self):
        if self.config.jobsConfig.sendMessagesJobActivated == True:
            SendMessage.sendMessage(
                self.channel_string, self.config.messagesConfig.pomStartMessage
            )
        time.sleep(1)
        id = ReceiveMessage().get_message_ids_with_searched_message(
            self.channel_string, self.config.messagesConfig.pomStartMessage
        )[0]
        if self.config.jobsConfig.reactEmojisJobActivated == True:
            ReactWithEmoji.react_with_emojis(
                id,
                self.channel_string,
                self.config.reactEmojisConfig.pomStartReactEmojis,
            )
        if self.config.jobsConfig.markOwnMessageUnreadActivated == True:
            MarkMessageUnread.markMessageUnread(self.channel_string, id)

    def _execute_end_messages(self):
        if self.config.jobsConfig.sendMessagesJobActivated == True:
            SendMessage.sendMessage(
                self.channel_string, self.config.messagesConfig.pomEndMessage
            )
        time.sleep(1)
        id = ReceiveMessage().get_message_ids_with_searched_message(
            self.channel_string, self.config.messagesConfig.pomEndMessage
        )[0]
        if self.config.jobsConfig.reactEmojisJobActivated == True:
            ReactWithEmoji.react_with_emojis(
                id, self.channel_string, self.config.reactEmojisConfig.pomEndReactEmojis
            )
        if self.config.jobsConfig.markOwnMessageUnreadActivated == True:
            MarkMessageUnread.markMessageUnread(self.channel_string, id)
        if self.config.jobsConfig.checkAfksJobActivated == True:
            CheckAfks.check_afks(self.channel_string, 7200)
