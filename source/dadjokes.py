from source.sendMessage import SendMessage
from dadjokes import Dadjoke

class DadJokesSender:
    @staticmethod
    def send_dad_joke(channelID):
        dadjoke = Dadjoke()
        SendMessage.sendMessage(channelID, f'DadJoke: {dadjoke.joke}')