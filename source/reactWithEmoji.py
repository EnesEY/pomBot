import requests
from project_secrets import token_secret
import time


class ReactWithEmoji:
    @staticmethod
    def _reactWithEmoji(channelID: str, messageID: str, emoji: str):
        header = {"authorization": token_secret}
        myString = channelID + "/" + str(messageID) + emoji
        requests.put(myString, headers=header)

    @staticmethod
    def react_with_emojis(messageID, channelID, emojis):
        for emoji in emojis:
            ReactWithEmoji._reactWithEmoji(channelID, messageID, emoji.value)
            time.sleep(1)
