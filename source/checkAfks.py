from source.receiveMessage import ReceiveMessage

class CheckAfks:

    @staticmethod
    def check_afks(channelID, maxSecondsOld):
        messages = ReceiveMessage().get_messages_of_age(channelID, maxSecondsOld)
        usernames_in_messages = [message["author"]["username"] for message in messages]
        unique_usernames = list(set([username for username in usernames_in_messages]))
        # get all members
        # 
        print('')