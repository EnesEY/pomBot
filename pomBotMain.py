from config.config import *
from source.reactEmojiLists import ReactEmojiLists
from source.pomBot import PomBot
import datetime
import logging
from logging import Logger
from source.messages import Messages
from pathlib import Path

# documentation https://discord.com/developers/docs/resources/channel#get-channel-messages
# help for setup in readme.md

my_config = Config(
    messagesConfig=MessagesConfig(
        sendMessagesJobActivated=True,
        pomStartMessage=Messages.sparkles_pom_start,
        pomEndMessage=Messages.dancing_bear_pom_end,
    ),  # pom start and end messages can be configured here
    reactEmojisConfig=ReactEmojisConfig(
        reactEmojisJobActivated=False,
        pomStartReactEmojis=ReactEmojiLists.sparkles,
        pomEndReactEmojis=ReactEmojiLists.numbers,
    ),  # lists with emojis that are reacted on pom start and end messages
    afkCheckConfig=AfkCheckConfig(
        checkAfksJobActivated=True, maxSecondsOld=8000
    ),  # if someone didn't send messages for maxSecondsOld they are marked as afk
    markOwnMessagesUnreadConfig=MarkOwnMessagesUnreadConfig(
        markOwnMessageUnreadActivated=False
    ),
    dadJokesConfig=DadJokesConfig(dadJokeJobActivated=False),  # activates dad jokes
    pomTimeConfig=PomTimeConfig(
        pom_duration=25,
        pom_break_duration=5,
        pom_start_time=30,
    ),  # configure pom timer
    channel_id=1186570188481626162,  # id of the dm-group
)


def get_secret_token(logger: Logger) -> str:
    token_file_path = Path("secret_token.txt")

    if token_file_path.exists():
        with token_file_path.open("r") as file:
            secret_token = file.read().strip()
    else:
        secret_token = input("Enter the secret token: ")
        with token_file_path.open("w") as file:
            file.write(secret_token)
        logger.info(f"Token saved to {token_file_path}")

    return secret_token


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s %(asctime)s:  %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    try:
        my_config.secret_token = get_secret_token(logger)
        pomBot = PomBot(my_config, logger)
        pomBot.start_cycle()
    except Exception as general_error:
        print(f"Unexpected error occurred: {general_error}")


if __name__ == "__main__":
    main()
