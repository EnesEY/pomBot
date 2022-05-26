from pomBot import PomBot
from pomBotSendMessage import PomBotSend


try:
    pomBotSend = PomBotSend()
    pomBot = PomBot(pomBotSend.startEmojiToTest, pomBotSend.doneEmojiToTest,1,1)
    pomBot.start_cycle()
except Exception as e:
    print('exception has occured')
    pomBot.stop_cycle()