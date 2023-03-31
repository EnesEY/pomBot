from dataclasses import dataclass
from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class PomTimeType(ExtendedEnum):
    POM_TIME_TYPE_DEFAULT_25 = (0,)
    POM_TIME_TYPE_DEFAULT_50 = (1,)
    POM_TIME_TYPE_CUSTOM = (2,)


@dataclass
class MessagesConfig:
    pomStartMessage: str
    pomEndMessage: str


@dataclass
class JobsConfig:
    sendMessagesJobActivated: bool
    reactEmojisJobActivated: bool
    markOwnMessageUnreadActivated: bool


@dataclass
class Config:
    messagesConfig: MessagesConfig
    jobsConfig: JobsConfig


default_25s_pom_config = Config(
    messagesConfig=MessagesConfig(
        pomStartMessage="@here <a:echat_sparkles:794309945414778881> <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_s:795783310206828548> <:p_letter_t:795783310563213363> <:p_letter_a:795783477269233724> <:p_letter_r:795783310630191104> <:p_letter_t:795783310563213363> <a:echat_sparkles:794309945414778881>",
        pomEndMessage="@here <a:SquirrelRolli:665618752322273280>  <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_d:795783310365294682> <:p_letter_o:795783310608957450> <:p_letter_n:795783310315880469> <:p_letter_e:795783310583791677>  <a:SquirrelRolli:665618752322273280> ",
    ),
    jobsConfig=JobsConfig(
        sendMessagesJobActivated=True,
        reactEmojisJobActivated=False,
        markOwnMessageUnreadActivated=False,
    ),
)
