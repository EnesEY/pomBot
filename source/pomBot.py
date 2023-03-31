from config.config import Config, JobsConfig, PomTimeType
from source.Jobs.reactEmojiJob import ReactEmojiJob
from source.Jobs.sendMessageJob import SendMessageJob
from typing import List
import datetime


class PomBot:
    channel_string: str
    auth_token: str
    config: Config
    jobs: List
    pomStartMin: int
    pomEndMin: int
    pomDurationInMin: int
    pomBreakTimeInMin: int

    def __init__(
        self,
        channel_id: int,
        secret_token: str,
        config: Config,
        pomTimeConfig: PomTimeType,
        pomStartMin=None,
        pomEndMin=None,
        pomDurationInMin=None,
        pomBreakTimeInMin=None,
    ):
        self.channel_string = self._get_channel_string(channel_id)
        self.pomStartMin = pomStartMin
        self.pomEndMin = pomEndMin
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.auth_token = secret_token
        self.config = config
        self._load_pom_times(pomTimeConfig)
        self.jobs = []
        self._get_project_jobs(config)

    def _get_channel_string(self, channel_id: int):
        channel_string_start = "https://discord.com/api/v9/channels/"
        channel_string_end = "/messages"
        return channel_string_start + str(channel_id) + channel_string_end

    def _load_pom_times(self, pomTimeConfig: PomTimeType):
        if pomTimeConfig == PomTimeType.POM_TIME_TYPE_DEFAULT_25:
            self.pomDurationInMin = 25
            self.pomBreakTimeInMin = 5
            if (
                datetime.datetime.now().minute % self.pomDurationInMin
            ) <= self.pomBreakTimeInMin:
                if datetime.datetime.now().minute > 31:
                    self.pomStartMin = 0
                    self.pomEndMin = 111
                else:
                    self.pomStartMin = 30
                    self.pomEndMin = 111
            else:
                if datetime.datetime.now().minute > 31:
                    self.pomStartMin = 111
                    self.pomEndMin = 55
                else:
                    self.pomStartMin = 111
                    self.pomEndMin = 25
        elif pomTimeConfig == PomTimeType.POM_TIME_TYPE_DEFAULT_50:
            self.pomDurationInMin = 50
            self.pomBreakTimeInMin = 10
            if datetime.datetime.now().minute > 50:
                self.pomStartMin = 0
                self.pomEndMin = 111
            else:
                self.pomStartMin = 111
                self.pomEndMin = 50

    def _get_project_jobs(self, config: Config):
        jobs_config = config.jobsConfig
        if jobs_config.sendMessagesJobActivated == True:
            send_message_job = SendMessageJob(
                self.channel_string,
                self.pomStartMin,
                self.pomEndMin,
                self.pomDurationInMin,
                self.pomBreakTimeInMin,
                config
            )
            self.jobs.append(send_message_job)
        if jobs_config.reactEmojisJobActivated == True:
            react_emoji_job = ReactEmojiJob(
                self.channel_string,
                self.pomStartMin,
                self.pomEndMin,
                self.pomDurationInMin,
                self.pomBreakTimeInMin,
                config
            )
            self.jobs.append(react_emoji_job)

    def start(self):
        for job in self.jobs:
            try:
                job.start_cycle()
            except Exception as e:
                print("exception has occured")
                job.stop_cycle()
