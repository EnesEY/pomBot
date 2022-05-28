from Enums.PomBotEnums import ConfigEnum


class PomConfig:
    def __init__(self, configEnum: ConfigEnum):
        if configEnum == ConfigEnum.CONFIG_FOR_MOWGLI_CHANNEL_25_5:
            self.pomDurationInMin = 25
            self.pomBreakTimeInMin = 5
        elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_2_1:
            self.pomDurationInMin = 2
            self.pomBreakTimeInMin = 1
        elif configEnum == ConfigEnum.CONFIG_FOR_TEST_CHANNEL_5_1:
            self.pomDurationInMin = 5
            self.pomBreakTimeInMin = 1
