import requests
from Enums.pomBotEnums import Payloads, ChannelIDs, AuthenticationTokens, ReactEmojis
import time

class PomBotReactEmojis:
    header = {
        'authorization': AuthenticationTokens.AUTH_TOKEN_1.value,
    }
 
    def __react_with_all(self, channelID, messageID):
        for emoji in ReactEmojis.list():
            myString = channelID + "/" +str(messageID) + emoji
            requests.put(myString, headers=self.header)
            time.sleep(1)

    def react_with_all_mogli(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value
        self.__react_with_all(channelID, messageID)  

    def react_with_all_Test(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_BOT_TEST.value
        self.__react_with_all(channelID, messageID)  
 
 
 
