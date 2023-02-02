import requests
from Enums.pomBotEnums import ReactEmojisSparkles, ReactEmojisNumbers
from project_secrets import token_secret
import time


class ReactWithEmoji:
    def reactWithEmoji(
        self, channelID: str, messageID: str, emoji: str, authToken: str
    ):
        header = {"authorization": authToken}
        myString = channelID + "/" + str(messageID) + emoji
        requests.put(myString, headers=header)

    def react_with_all_sparkles(self, messageID, channelID):
        for emoji in ReactEmojisSparkles.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)

    def react_with_all_numbers(self, messageID, channelID):
        for emoji in ReactEmojisNumbers.list():
            self.reactWithEmoji(channelID, messageID, emoji, token_secret)
            time.sleep(1)
