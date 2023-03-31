from config.config import default_25s_pom_config, PomTimeType
from source.pomBot import PomBot
from project_secrets import token_secret


def main():
    pomBot = PomBot(
        channel_id=1091469223009726575,
        secret_token=token_secret,
        pomTimeConfig=PomTimeType.POM_TIME_TYPE_DEFAULT_25,
        config=default_25s_pom_config,
        # only needed if pomTimeConfig=PomTimeType.POM_TIME_TYPE_CUSTOM
        # pomStartMin=19,
        # pomEndMin=111,
        # pomDurationInMin=2,
        # pomBreakTimeInMin=1,
    )
    pomBot.start()


if __name__ == "__main__":
    main()
