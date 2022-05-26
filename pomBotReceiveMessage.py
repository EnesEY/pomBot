import requests
from pomBotEnums import Payloads, ChannelIDs, AuthenticationTokens

class PomBotReceive:
    def __receivePomMessage(self, channelID: str, authToken: str):
        header = {
            'authorization': authToken
        }
        requests.post(channelID, data=payload, headers=header)
        print('sent message')

    def startEmojiToTest(self):
        self.__sendPomMessage(ChannelIDs.CHANNEL_ID_BOT_TEST.value, Payloads.PAYLOAD_POM_START_EMOJI.value, AuthenticationTokens.AUTH_TOKEN_1.value)
