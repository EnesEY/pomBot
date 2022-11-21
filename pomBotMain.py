from source.Jobs.reactEmojiJob import ReactEmojiJob
from source.Jobs.sendMessageJob import SendMessageJob
import utils

if __name__ == "__main__":
    # set the one to the value you want and the other to 999
    pomStartMin = 333  # if you wanna start with a pom START
    pomEndMin = 50  # if you wanna start with a pom end

    channel_id = 1044050144917737522  # mowgli dm-group
    channel_string = utils.get_channel_string(channel_id)

    pomDurationInMin = 50
    pomBreakTimeInMin = 10

    pomBotSendJob = SendMessageJob(channel_string, pomStartMin, pomEndMin, pomDurationInMin, pomBreakTimeInMin)
    #pomBotReactJob = ReactEmojiJob(channel_string, pomStartMin, pomEndMin, pomDurationInMin, pomBreakTimeInMin)
    try:
        pomBotSendJob.start_cycle()
        #pomBotReactJob.start_cycle()
    except Exception as e:
        print("exception has occured")
        pomBotSendJob.stop_cycle()
        #pomBotReactJob.stop_cycle()
