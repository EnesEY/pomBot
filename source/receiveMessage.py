from typing import List
import requests
import json
from datetime import datetime
from dateutil.parser import parse
from project_secrets import token_secret


class ReceiveMessage:
    def __retrieveAllMessages(self, channelID: str, limit: int):
        header = {"authorization": token_secret}
        payload = {"limit": limit}
        response = requests.get(channelID, headers=header, params=payload)
        return response

    def __filterJSONResponseForMessagesOfUser(self, jsonResponse, userName: str):
        filtered_data = []
        for data in jsonResponse:
            if data["author"]["username"] == userName:
                filtered_data.append(data)
        return filtered_data

    def __filterMessageListForAge(self, messageList: List, maxSecondsOld: int):
        filtered_data = []
        for data in messageList:
            timestamp_1 = parse(data["timestamp"]).timestamp()
            timestamp_2 = datetime.now().timestamp()
            t_diff = timestamp_2 - timestamp_1
            if t_diff < maxSecondsOld:
                filtered_data.append(data)
        return filtered_data

    def get_message_ids_with_searched_message(
        self,
        channelID: str,
        searched_message: str,
        limit: int = 100,
    ):
        messages_with_limit = self.__retrieveAllMessages(channelID, limit)
        json_data = json.loads(messages_with_limit.text)
        messages_with_searched_payload = []
        for data in json_data:
            if data["content"] == searched_message:
                messages_with_searched_payload.append(data["id"])
        return messages_with_searched_payload

    def get_message_ids_with_username(
        self,
        channelID: str,
        userName: str,
        maxSecondsOld: int = None,
        limit: int = 100,
    ):
        user_message_list = []
        messages_with_limit = self.__retrieveAllMessages(channelID, limit)
        json_data = json.loads(messages_with_limit.text)
        user_message_list = self.__filterJSONResponseForMessagesOfUser(
            json_data, userName
        )
        if maxSecondsOld is not None:
            user_message_list = self.__filterMessageListForAge(
                user_message_list, maxSecondsOld
            )
        return [message["id"] for message in user_message_list]

    def get_messages_of_age(self, channelID: str, maxSecondsOld: int, limit: int = 100):
        messages_with_limit = self.__retrieveAllMessages(channelID, limit)
        json_data = json.loads(messages_with_limit.text)
        messages_of_age = self.__filterMessageListForAge(json_data, maxSecondsOld)
        return messages_of_age

    def getRecipients(
        self, channelID: str
    ):  # endpoint does not work, only works for bots
        header = {"authorization": token_secret}
        channelID = channelID + "/recipients"
        response = requests.get(channelID, headers=header)
        json_data = json.loads(response.text)
        return json_data
