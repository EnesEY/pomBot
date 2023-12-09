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
    pomTimeConfig=PomTimeConfig(
        pom_duration=25,
        pom_break_duration=5,
        # pom_start_time=datetime.datetime.now().minute,
    ),
    channel_id=1182833837483511949,
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
    logging.basicConfig(level=logging.INFO)
    logger: Logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    try:
        my_config.secret_token = get_secret_token(logger)
        pomBot = PomBot(my_config, logger)
        pomBot.start_cycle()
    except Exception as general_error:
        print(f"Unexpected error occurred: {general_error}")


if __name__ == "__main__":
    main()
