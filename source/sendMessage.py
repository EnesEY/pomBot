import requests
from Enums.pomBotEnums import Payloads
from project_secrets import token_secret


class SendMessage:
    def sendMessage(self, channelID: str, payload: str, authToken: str):
        payload = {"content": payload}
        header = {"authorization": authToken}
        requests.post(channelID, data=payload, headers=header)
        print(f"message was sent to channelID: {channelID}")

    def sendStartMessage(self, channel_string):
        self.sendMessage(
            channel_string, Payloads.PAYLOAD_POM_START_EMOJI.value, token_secret
        )

    def sendEndMessage(self, channel_string):
        self.sendMessage(
            channel_string, Payloads.PAYLOAD_POM_DONE_EMOJI.value, token_secret
        )
