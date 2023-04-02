import requests
from project_secrets import token_secret
import json


class MarkMessageUnread:
    @staticmethod
    def markMessageUnread(channelID: str, messageID: str):
        payload = {"manual": True, "mention_count": 1}
        json_object = json.dumps(payload)
        header = {"authorization": token_secret, "Content-Type": "application/json"}
        myString = channelID + "/" + str(messageID) + "/ack"
        output = requests.post(myString, data=json_object, headers=header)
        print(f"message {messageID} was marked unread")
