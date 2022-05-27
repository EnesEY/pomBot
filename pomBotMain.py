from Jobs.pomBotReactEmojisJob import PomBotReactEmojisJob
from Jobs.pomBotSendJob import PomBotSendJob
from pomBotSendMessage import PomBotSend
from pomBotReceiveMessage import PomBotReceive
from pomBotReactEmojis import PomBotReactEmojis
from Config.pom_config import PomConfig

try:
    pomDuratingInMin = 25
    pomBreakInMin = 5
    pomStartMin = 30
    myConfig = PomConfig.
    pomBotSend = PomBotSend()
    pomBotReceive = PomBotReceive()
    pomBotReact = PomBotReactEmojis()
    pomBotSendJob = PomBotSendJob(pomBotSend.startEmojiToMogli, pomBotSend.doneEmojiToMogli,pomDuratingInMin,pomBreakInMin, pomStartMin)
    pomBotReactJob = PomBotReactEmojisJob(pomDuratingInMin,pomBreakInMin,pomBotReceive.getLastMessageIDMogli,pomBotReact.react_with_all_mogli, pomStartMin)
    pomBotSendJob.start_cycle()
    pomBotReactJob.start_cycle()
except Exception as e:
    print('exception has occured')
    pomBotSendJob.stop_cycle()
    pomBotReactJob.stop_cycle()