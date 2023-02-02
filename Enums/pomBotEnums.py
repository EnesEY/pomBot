from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Payloads(ExtendedEnum):
    PAYLOAD_POM_START_1 = "@here pom start"
    PAYLOAD_POM_DONE_1 = "@here pom done"
    PAYLOAD_POM_START_EMOJI = "@here <a:echat_sparkles:794309945414778881> <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_s:795783310206828548> <:p_letter_t:795783310563213363> <:p_letter_a:795783477269233724> <:p_letter_r:795783310630191104> <:p_letter_t:795783310563213363> <a:echat_sparkles:794309945414778881>"
    PAYLOAD_POM_DONE_EMOJI = "@here <a:SquirrelRolli:665618752322273280>  <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_d:795783310365294682> <:p_letter_o:795783310608957450> <:p_letter_n:795783310315880469> <:p_letter_e:795783310583791677>  <a:SquirrelRolli:665618752322273280> "


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
