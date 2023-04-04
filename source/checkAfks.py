from source.receiveMessage import ReceiveMessage
from source.sendMessage import SendMessage


class CheckAfks:
    @staticmethod
    def check_afks(channelID, maxSecondsOld):
        messages = ReceiveMessage().getAllMessagesInTimeframe(channelID, maxSecondsOld)
        usernames_in_messages = [
            username["author"]["username"] for username in messages
        ]
        unique_usernames = list(set(usernames_in_messages))
        recipients = ReceiveMessage().getRecipients(channelID)
        missing_names = list(set(recipients) - set(unique_usernames))
        info_str = ""
        for name in missing_names:
            info_str += name + " "
        if info_str != "":
            SendMessage.sendMessage(channelID, f"users: {info_str}seem to be afk")
