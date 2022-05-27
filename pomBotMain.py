from Jobs.pomBotReactEmojisJob import PomBotReactEmojisJob
from Jobs.pomBotSendJob import PomBotSendJob
from pom_config import PomConfigInterface

pomStartMin = 25
pomEndMin = 2
myConfig = PomConfigInterface.get_mowgli_25_5_sparkle_config()
pomBotSendJob = PomBotSendJob(myConfig, pomStartMin, pomEndMin)
pomBotReactJob = PomBotReactEmojisJob(myConfig, pomStartMin, pomEndMin)
try:
    pomBotSendJob.start_cycle()
    pomBotReactJob.start_cycle()
except Exception as e:
    print('exception has occured')
    pomBotSendJob.stop_cycle()
    pomBotReactJob.stop_cycle()