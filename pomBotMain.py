from Jobs.pomBotReactEmojisJob import PomBotReactEmojisJob
from Jobs.pomBotSendJob import PomBotSendJob
from pom_config import PomConfigInterface

# set the one to the value you want and the other to 999
pomStartMin = 999  # if you wanna start with a pom START
pomEndMin = 33  # if you wanna start with a pom end

myConfig = PomConfigInterface.get_test_2_1_sparkle_config()
pomBotSendJob = PomBotSendJob(myConfig, pomStartMin, pomEndMin)
pomBotReactJob = PomBotReactEmojisJob(myConfig, pomStartMin, pomEndMin)
try:
    pomBotSendJob.start_cycle()
    pomBotReactJob.start_cycle()
except Exception as e:
    print("exception has occured")
    pomBotSendJob.stop_cycle()
    pomBotReactJob.stop_cycle()
