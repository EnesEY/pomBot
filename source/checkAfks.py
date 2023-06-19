from source.receiveMessage import ReceiveMessage
from source.sendMessage import SendMessage


class CheckAfks:
    @staticmethod
    def check_afks(channelID, maxSecondsOld):
        messages = ReceiveMessage().getAllMessagesInTimeframe(channelID, maxSecondsOld)
        authors = [subdict["author"] for subdict in messages]
        usernames = [d.get("global_name") or d.get("username") for d in authors if "username" in d or "global_name" in d]
        unique_usernames = list(set(usernames))
        recipients = ReceiveMessage().getRecipients(channelID)
        missing_usernames = list(set(recipients) - set(unique_usernames))
        info_str = ""
        for name in missing_usernames:
            info_str += name + " "
        if info_str != "":
            SendMessage.sendMessage(channelID, f"users: {info_str}seem to be afk")
