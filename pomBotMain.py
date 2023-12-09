from config.config import *
from source.reactEmojiLists import ReactEmojiLists
from source.pomBot import PomBot
from project_secrets import token_secret
import datetime
import logging
from logging import Logger

# documentation https://discord.com/developers/docs/resources/channel#get-channel-messages
# help for setup in readme.md

my_config = Config(
    messagesConfig=MessagesConfig(
        sendMessagesJobActivated=True,
        pomStartMessage="@here <a:echat_sparkles:794309945414778881> <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_s:795783310206828548> <:p_letter_t:795783310563213363> <:p_letter_a:795783477269233724> <:p_letter_r:795783310630191104> <:p_letter_t:795783310563213363> <a:echat_sparkles:794309945414778881>",
        pomEndMessage="@here <a:SquirrelRolli:665618752322273280>  <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_d:795783310365294682> <:p_letter_o:795783310608957450> <:p_letter_n:795783310315880469> <:p_letter_e:795783310583791677>  <a:SquirrelRolli:665618752322273280>",
    ),
    reactEmojisConfig=ReactEmojisConfig(
        reactEmojisJobActivated=True,
        pomStartReactEmojis=ReactEmojiLists.sparkles,
        pomEndReactEmojis=ReactEmojiLists.numbers,
    ),
    afkCheckConfig=AfkCheckConfig(
        checkAfksJobActivated=True, maxSecondsOld=8000
    ),  # 2h 5400
    markOwnMessagesUnreadConfig=MarkOwnMessagesUnreadConfig(
        markOwnMessageUnreadActivated=True
    ),
    dadJokesConfig=DadJokesConfig(dadJokeJobActivated=True),
    secret_token=token_secret,
    pomTimeConfig=PomTimeConfig(
        pom_duration=25,
        pom_break_duration=5,
        # pom_start_time=datetime.datetime.now().minute,
    ),
    channel_id=1182833837483511949,
)


def main():
    try:
        logging.basicConfig(level=logging.INFO)
        logger: Logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        pomBot = PomBot(my_config, logger)
        pomBot.start_cycle()
    except Exception as general_error:
        print(f"Unexpected error occurred: {general_error}")


if __name__ == "__main__":
    main()
