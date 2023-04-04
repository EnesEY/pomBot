from dataclasses import dataclass
from Enums.pomBotEnums import ExtendedEnum
import abc


class PomTimeType(ExtendedEnum):
    POM_TIME_TYPE_DEFAULT_25 = (0,)
    POM_TIME_TYPE_DEFAULT_50 = (1,)
    POM_TIME_TYPE_CUSTOM = (2,)


@dataclass
class MessagesConfig:
    pomStartMessage: str
    pomEndMessage: str


@dataclass
class ReactEmojisConfig:
    pomStartReactEmojis: ExtendedEnum
    pomEndReactEmojis: ExtendedEnum


@dataclass
class AfkCheckConfig:
    maxSecondsOld: int


@dataclass
class JobsConfig:
    sendMessagesJobActivated: bool
    reactEmojisJobActivated: bool
    markOwnMessageUnreadActivated: bool
    checkAfksJobActivated: bool


@dataclass
class Config:
    messagesConfig: MessagesConfig
    jobsConfig: JobsConfig
    reactEmojisConfig: ReactEmojisConfig
    afkCheckConfig: AfkCheckConfig
