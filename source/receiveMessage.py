from typing import List
import requests
import json
from datetime import datetime
from dateutil.parser import parse
from Enums.pomBotEnums import Payloads
from project_secrets import token_secret


class ReceiveMessage:
    # data["author"]["username"] -> "author"
    usedFieldsInMessages = ["id", "content", "author", "timestamp"]

    def __retrieveAllMessages(self, channelID: str, authToken: str, limit: int):
        header = {"authorization": authToken}
        payload = {"limit": limit}
        response = requests.get(channelID, headers=header, params=payload)
        return response

    def __convertHttpResponseToJSON(self, httpResponse):
        json_data = json.loads(httpResponse.text)
        return json_data

    def __filterJSONResponseForMessagesOfUser(self, jsonResponse, userName: str):
        filtered_data = []
        for data in jsonResponse:
            if (data["content"] in Payloads.list()) and data["author"]["username"] == userName:
                filtered_data.append(data)
        return filtered_data

    def __filterMessageListForAge(self, messageList: List,  maxSecondsOld: int):
        filtered_data = []
        for data in messageList:
            timestamp_1 = parse(data["timestamp"]).timestamp()
            timestamp_2 = datetime.now().timestamp()
            if (timestamp_2 - timestamp_1) < maxSecondsOld:
                filtered_data.append(data)
        return filtered_data

    def __filterMessageListForUsedFields(self, messageList: List, fields):
        filtered_data = []
        for data in messageList:
            this_message = {}
            for field in fields:
                if field == "author":
                    this_message["username"] = data["author"]["username"]
                else:
                    this_message[field] = data[field]
            filtered_data.append(this_message)
        return filtered_data

    def receiveBotMessages(self, channelID: str, authToken: str, limit: int, botUserName: str, maxSecondsOld: int):
        all_messages = self.__retrieveAllMessages(channelID, authToken, limit)
        json_data = self.__convertHttpResponseToJSON(all_messages)
        user_message_list = self.__filterJSONResponseForMessagesOfUser(json_data, botUserName)
        user_message_list = self.__filterMessageListForAge(user_message_list, maxSecondsOld)
        user_message_list = self.__filterMessageListForUsedFields(user_message_list, self.usedFieldsInMessages)
        print(f'retrieved messages of bot: {botUserName} that are max. {maxSecondsOld} seconds old')
        return user_message_list

    def get_last_bot_message_id_in_last_150_seconds(self, channel_string):
        messageID = 0
        messages = self.receiveBotMessages(channel_string, token_secret, 5, "EnesEY", 150)
        for message in messages:
            messageID = message["id"]
        return messageID
