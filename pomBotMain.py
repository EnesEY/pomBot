from config.config import (
    Config,
    MessagesConfig,
    JobsConfig,
    PomTimeType,
    ReactEmojisConfig,
)
from Enums.pomBotEnums import ReactEmojisSparkles, ReactEmojisNumbers
from source.pomBot import PomBot
from project_secrets import token_secret
import datetime

# documentation https://discord.com/developers/docs/resources/channel#get-channel-messages

my_config = Config(
    messagesConfig=MessagesConfig(
        pomStartMessage="@here <a:echat_sparkles:794309945414778881> <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_s:795783310206828548> <:p_letter_t:795783310563213363> <:p_letter_a:795783477269233724> <:p_letter_r:795783310630191104> <:p_letter_t:795783310563213363> <a:echat_sparkles:794309945414778881>",
        pomEndMessage="@here <a:SquirrelRolli:665618752322273280>  <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_d:795783310365294682> <:p_letter_o:795783310608957450> <:p_letter_n:795783310315880469> <:p_letter_e:795783310583791677>  <a:SquirrelRolli:665618752322273280>",
    ),
    jobsConfig=JobsConfig(
        sendMessagesJobActivated=True,
        reactEmojisJobActivated=True,
        markOwnMessageUnreadActivated=True,
        checkAfksJobActivated=True,
    ),
    reactEmojisConfig=ReactEmojisConfig(  # only used if reactEmojisJobActivated == True
        pomStartReactEmojis=ReactEmojisSparkles, pomEndReactEmojis=ReactEmojisNumbers
    ),
)


def main():
    pomBot = PomBot(
        channel_id=1084544283786350624,
        secret_token=token_secret,
        pomTimeConfig=PomTimeType.POM_TIME_TYPE_DEFAULT_25,  # POM_TIME_TYPE_DEFAULT_25 , POM_TIME_TYPE_DEFAULT_50, POM_TIME_TYPE_CUSTOM
        config=my_config,
        # only relevant if pomTimeConfig=PomTimeType.POM_TIME_TYPE_CUSTOM
        pomStartMin=111,
        pomEndMin=datetime.datetime.now().minute,
        pomDurationInMin=2,
        pomBreakTimeInMin=1,
    )
    try:
        pomBot.start_cycle()
    except:
        print("something went wrong")


if __name__ == "__main__":
    main()
