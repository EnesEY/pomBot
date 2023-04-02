from source.receiveMessage import ReceiveMessage


class CheckAfks:
    @staticmethod
    def check_afks(channelID, maxSecondsOld):
        messages = ReceiveMessage().get_messages_of_age(channelID, maxSecondsOld)
        recipients = ReceiveMessage().getRecipients(
            channelID
        )  # endpoint does not work, only works for bots
