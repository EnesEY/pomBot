import requests
from project_secrets import token_secret


class SendMessage:
    @staticmethod
    def sendMessage(channelID: str, payload: str):
        payload = {"content": payload}
        header = {"authorization": token_secret}
        requests.post(channelID, data=payload, headers=header)
        print(f"message was sent to channelID: {channelID}")
