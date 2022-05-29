import requests
from Enums.pomBotEnums import ConfigEnum, ChannelIDs, ReactEmojisSparkles, ReactEmojisNumbers
from project_secrets import token_secret
import time


class ReactWithEmoji:
    def reactWithEmoji(self, channelID: str, messageID: str, emoji: str, authToken: str):
        header = {"authorization": authToken}
        myString = channelID + "/" + str(messageID) + emoji
        requests.put(myString, headers=header)

    def getReactWithEmojiFunction(self, configEnum: ConfigEnum, isStart: bool):
        if isStart == True:
            if configEnum == ConfigEnum.CONFIG_FOR_MOWGLI_CHANNEL_25_5:
                return self.react_with_all_sparkles_mowgli
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1:
                return self.react_with_all_sparkles_test
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_5_1:
                return self.react_with_all_sparkles_test
            else:
                print('ERROR')
        elif isStart == False:
            if configEnum == ConfigEnum.CONFIG_FOR_MOWGLI_CHANNEL_25_5:
                return self.react_with_all_numbers_mowgli
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1:
                return self.react_with_all_numbers_test
            elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_5_1:
                return self.react_with_all_numbers_test
            else:
                print('ERROR')
        else:
            print('ERROR')

    def react_with_all_sparkles_mowgli(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value
        for emoji in ReactEmojisSparkles.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)

    def react_with_all_numbers_mowgli(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_MOWGLI_DM_GROUP.value
        for emoji in ReactEmojisNumbers.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)

    def react_with_all_sparkles_test(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_BOT_TEST.value
        for emoji in ReactEmojisSparkles.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)

    def react_with_all_numbers_test(self, messageID):
        channelID = ChannelIDs.CHANNEL_ID_BOT_TEST.value
        for emoji in ReactEmojisNumbers.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)
