import requests
from Enums.pomBotEnums import Payloads, ChannelIDs, AuthenticationTokens

class PomBotSend:
    def __sendPomMessage(self, channelID: str, payload: str, authToken: str):
        payload = {
            'content': payload
        }
        header = {
            'authorization': authToken
        }
        requests.post(channelID, data=payload, headers=header)
        print('sent message')

    def startEmojiToTest(self):
        self.__sendPomMessage(ChannelIDs.CHANNEL_ID_BOT_TEST.value, Payloads.PAYLOAD_POM_START_EMOJI.value, AuthenticationTokens.AUTH_TOKEN_1.value)

    def doneEmojiToTest(self):
        self.__sendPomMessage(ChannelIDs.CHANNEL_ID_BOT_TEST.value, Payloads.PAYLOAD_POM_DONE_EMOJI.value, AuthenticationTokens.AUTH_TOKEN_1.value)

    def startEmojiToMogli(self):
        self.__sendPomMessage(ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value, Payloads.PAYLOAD_POM_START_EMOJI.value, AuthenticationTokens.AUTH_TOKEN_1.value)

    def doneEmojiToMogli(self):
        self.__sendPomMessage(ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value, Payloads.PAYLOAD_POM_DONE_EMOJI.value, AuthenticationTokens.AUTH_TOKEN_1.value)






