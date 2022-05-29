import requests
from Enums.pomBotEnums import ConfigEnum, ChannelIDs, Payloads
from project_secrets import token_secret


class SendMessage:
    def sendMessage(self, channelID: str, payload: str, authToken: str):
        payload = {"content": payload}
        header = {"authorization": authToken}
        requests.post(channelID, data=payload, headers=header)
        print(f'message was sent to channelID: {channelID}')

    def getSendMessageFunction(self, configEnum: ConfigEnum, isStart: bool):
        if isStart == True:
            if configEnum == ConfigEnum.CONFIG_FOR_MOWGLI_CHANNEL_25_5:
                return self.sendStartMessageToMowgli
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1:
                return self.sendStartMessageToTest
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_5_1:
                return self.sendStartMessageToTest
            else:
                print('ERROR')
        elif isStart == False:
            if configEnum == ConfigEnum.CONFIG_FOR_MOWGLI_CHANNEL_25_5:
                return self.sendEndMessageToMowgli
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1:
                return self.sendEndMessageToTest
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_5_1:
                return self.sendEndMessageToTest
            else:
                print('ERROR')
        else:
            print('ERROR')

    def sendStartMessageToTest(self):
        self.sendMessage(ChannelIDs.CHANNEL_ID_BOT_TEST.value,
                         Payloads.PAYLOAD_POM_START_EMOJI.value, token_secret)

    def sendEndMessageToTest(self):
        self.sendMessage(ChannelIDs.CHANNEL_ID_BOT_TEST.value,
                         Payloads.PAYLOAD_POM_DONE_EMOJI.value, token_secret)

    def sendStartMessageToMowgli(self):
        self.sendMessage(ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value,
                         Payloads.PAYLOAD_POM_START_EMOJI.value, token_secret)

    def sendEndMessageToMowgli(self):
        self.sendMessage(ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value,
                         Payloads.PAYLOAD_POM_DONE_EMOJI.value, token_secret)
