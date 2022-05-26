from enum import Enum
import config

class Payloads(Enum):
    PAYLOAD_POM_START_1 = "@here pom start"
    PAYLOAD_POM_DONE_1  = "@here pom done"
    PAYLOAD_POM_START_EMOJI = "@here <a:echat_sparkles:794309945414778881> <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_s:795783310206828548> <:p_letter_t:795783310563213363> <:p_letter_a:795783477269233724> <:p_letter_r:795783310630191104> <:p_letter_t:795783310563213363> <a:echat_sparkles:794309945414778881>"
    PAYLOAD_POM_DONE_EMOJI = "@here <a:SquirrelRolli:665618752322273280>  <:p_letter_p:795783313242980372> <:p_letter_o:795783310608957450> <:p_letter_m:795783310483783691>     <:p_letter_d:795783310365294682> <:p_letter_o:795783310608957450> <:p_letter_n:795783310315880469> <:p_letter_e:795783310583791677>  <a:SquirrelRolli:665618752322273280>"

class ChannelIDs(Enum):
    CHANNEL_ID_MOWGLI_DM_GROUP = "https://discord.com/api/v9/channels/969415933779120180/messages"
    CHANNEL_ID_BOT_TEST = "https://discord.com/api/v9/channels/979459987866800168/messages"

class AuthenticationTokens(Enum):
    AUTH_TOKEN_1 = config.token_secret