from dataclasses import dataclass
from enum import Enum
from typing import List


class PomTimeType(Enum):
    POM_TIME_TYPE_DEFAULT_25 = 0
    POM_TIME_TYPE_DEFAULT_50 = 1
    POM_TIME_TYPE_DEBUG = 2


@dataclass
class MessagesConfig:
    sendMessagesJobActivated: bool
    pomStartMessage: str
    pomEndMessage: str


@dataclass
class ReactEmojisConfig:
    reactEmojisJobActivated: bool
    pomStartReactEmojis: List[str]
    pomEndReactEmojis: List[str]


@dataclass
class AfkCheckConfig:
    checkAfksJobActivated: bool
    maxSecondsOld: int


@dataclass
class MarkOwnMessagesUnreadConfig:
    markOwnMessageUnreadActivated: bool


@dataclass
class DadJokesConfig:
    dadJokeJobActivated: bool


@dataclass
class PomTimeConfig:
    pom_duration: int
    pom_break_duration: int
    pom_start_time: int = 0


@dataclass
class Config:
    messagesConfig: MessagesConfig
    reactEmojisConfig: ReactEmojisConfig
    afkCheckConfig: AfkCheckConfig
    markOwnMessagesUnreadConfig: MarkOwnMessagesUnreadConfig
    dadJokesConfig: DadJokesConfig
    pomTimeConfig: PomTimeConfig
    secret_token: str
    channel_id: int
