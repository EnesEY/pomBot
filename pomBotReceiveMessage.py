from pyexpat.errors import messages
import requests
from Enums.pomBotEnums import Payloads, ChannelIDs, AuthenticationTokens
import json
from datetime import datetime
from dateutil.parser import parse

class PomBotReceive:
    def __getAllMessages(self, channelID: str, authToken: str, limit:int):
        header = {
            'authorization': authToken,
        }
        payload = {
            'limit': limit
        }
        response = requests.get(channelID, headers=header,params=payload)
        json_data = json.loads(response.text)
        return json_data

    def __getBotMessages(self, max_seconds_old, messages_searched_limit, channelID):
        bot_messages = {}
        print(f'searching in the last {messages_searched_limit} messages of the channel for messages from bot that are max. {max_seconds_old} seconds old')
        json_data = self.__getAllMessages(channelID, AuthenticationTokens.AUTH_TOKEN_1.value, messages_searched_limit)
        # filter for bot messages that are max_seconds_old
        for data in json_data:
            if (data['content'] in Payloads.list()) and data['author']['username'] == "EnesEY": # check if message is one from out bot
                timestamp_1 = parse(data['timestamp']).timestamp()
                timestamp_2 = datetime.now().timestamp()
                if (timestamp_2 - timestamp_1) < max_seconds_old: #max. 2.5min old
                    this_message = {
                        "id": data['id'],
                        "content": data['content'],
                        "username": data['author']['username'],
                        "timestamp": data['timestamp']
                    }
                    bot_messages[data['id']] = this_message
        return bot_messages

    def getLastMessageIDMogli(self):
        ids = ""
        channelID = ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value
        messages = self.__getBotMessages(150, 15,channelID)
        for message in messages:
            ids = str(messages[message]['id'])
        return ids

    def getLastMessageIDTest(self):
        ids = ""
        channelID = ChannelIDs.CHANNEL_ID_BOT_TEST.value
        messages = self.__getBotMessages(150, 15,channelID)
        for message in messages:
            ids = str(messages[message]['id'])
        return ids