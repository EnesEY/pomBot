from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class ReactEmojisSparkles(ExtendedEnum):
    REACT_EMOJI_KAWAII_SPARKLE = (
        "/reactions/kawaiiSparkles%3A737449279869681674/%40me?location=Message"
    )
    REACT_EMOJI_E_CHAT_SPARKLE = (
        "/reactions/echat_sparkles%3A794309945414778881/%40me?location=Message"
    )
    REACT_EMOJI_E_CHAT_SPARKLE_1 = (
        "/reactions/echat_sparkles~1%3A798665649504780388/%40me?location=Message"
    )
    REACT_EMOJI_P_SPARKLE = (
        "/reactions/p_sparkles03%3A771538649028362310/%40me?location=Message"
    )
    REACT_EMOJI_P_SPARKLE_01 = (
        "/reactions/p_sparkles01%3A735706323198541904/%40me?location=Message"
    )
    REACT_EMOJI_P_SPARKLE_04 = (
        "/reactions/p_sparkles04%3A771539740657844225/%40me?location=Message"
    )


class ReactEmojisNumbers(ExtendedEnum):
    REACT_EMOJI_NUMBER_0 = "/reactions/0%EF%B8%8F%E2%83%A3/%40me?location=Message"
    REACT_EMOJI_NUMBER_1 = "/reactions/1%EF%B8%8F%E2%83%A3/%40me?location=Message"
    REACT_EMOJI_NUMBER_2 = "/reactions/2%EF%B8%8F%E2%83%A3/%40me?location=Message"
    REACT_EMOJI_NUMBER_3 = "/reactions/3%EF%B8%8F%E2%83%A3/%40me?location=Message"
    REACT_EMOJI_NUMBER_4 = "/reactions/4%EF%B8%8F%E2%83%A3/%40me?location=Message"
    REACT_EMOJI_NUMBER_5 = "/reactions/5%EF%B8%8F%E2%83%A3/%40me?location=Message"
