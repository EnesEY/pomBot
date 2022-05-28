from source.Jobs.reactEmojiJob import ReactEmojiJob
from source.Jobs.sendMessageJob import SendMessageJob
from Enums.PomBotEnums import ConfigEnum

# set the one to the value you want and the other to 999
pomStartMin = 999  # if you wanna start with a pom START
pomEndMin = 8  # if you wanna start with a pom end

type = ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1
pomBotSendJob = SendMessageJob(type, pomStartMin, pomEndMin)
pomBotReactJob = ReactEmojiJob(type, pomStartMin, pomEndMin)
try:
    pomBotSendJob.start_cycle()
    pomBotReactJob.start_cycle()
except Exception as e:
    print("exception has occured")
    pomBotSendJob.stop_cycle()
    pomBotReactJob.stop_cycle()
