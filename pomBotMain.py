from Jobs.pomBotReactEmojisJob import PomBotReactEmojisJob
from Jobs.pomBotSendJob import PomBotSendJob
from pomBotSendMessage import PomBotSend
from pomBotReceiveMessage import PomBotReceive
from pomBotReactEmojis import PomBotReactEmojis


try:
    pomBotSend = PomBotSend()
    pomBotReceive = PomBotReceive()
    pomBotReact = PomBotReactEmojis()
    pomBotSendJob = PomBotSendJob(pomBotSend.startEmojiToMogli, pomBotSend.doneEmojiToMogli,25,5)
    pomBotReactJob = PomBotReactEmojisJob(25,5,pomBotReceive.getLastMessageIDMogli,pomBotReact.react_with_all_mogli)
    pomBotSendJob.start_cycle()
    pomBotReactJob.start_cycle()
except Exception as e:
    print('exception has occured')
    pomBotSendJob.stop_cycle()
    pomBotReactJob.stop_cycle()