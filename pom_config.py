from typing import Callable
from pomBotSendMessage import PomBotSend
from pomBotReceiveMessage import PomBotReceive
from pomBotReactEmojis import PomBotReactEmojis


class PomConfig:
    def __init__(
        self,
        pomStartFunction: Callable,
        pomEndFunction: Callable,
        pomDurationInMin: int,
        pomBreakTimeInMin: int,
        pomReceiveFunction: Callable,
        pomReactFunctionStart: Callable,
        pomReactFunctionEnd: Callable,
    ):
        self.pomStartFunction = pomStartFunction
        self.pomEndFunction = pomEndFunction
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.pomReceiveFunction = pomReceiveFunction
        self.pomReactFunctionStart = pomReactFunctionStart
        self.pomReactFunctionEnd = pomReactFunctionEnd


class PomConfigInterface:
    def get_mowgli_25_5_sparkle_config():
        mowgli_25_5_sparkle = PomConfig(
            pomStartFunction=PomBotSend().startEmojiToMogli,
            pomEndFunction=PomBotSend().doneEmojiToMogli,
            pomDurationInMin=25,
            pomBreakTimeInMin=5,
            pomReceiveFunction=PomBotReceive().getLastMessageIDMogli,
            pomReactFunctionStart=PomBotReactEmojis().react_with_all_mogli,
            pomReactFunctionEnd=PomBotReactEmojis().react_with_Numbers_mogli,
        )
        return mowgli_25_5_sparkle

    def get_test_2_1_sparkle_config():
        test_2_1_sparkle = PomConfig(
            pomStartFunction=PomBotSend().startEmojiToTest,
            pomEndFunction=PomBotSend().doneEmojiToTest,
            pomDurationInMin=2,
            pomBreakTimeInMin=1,
            pomReceiveFunction=PomBotReceive().getLastMessageIDTest,
            pomReactFunctionStart=PomBotReactEmojis().react_with_all_Test,
            pomReactFunctionEnd=PomBotReactEmojis().react_with_Numbers_Test,
        )
        return test_2_1_sparkle

    def get_test_5_1_sparkle_config():
        test_2_1_sparkle = PomConfig(
            pomStartFunction=PomBotSend().startEmojiToTest,
            pomEndFunction=PomBotSend().doneEmojiToTest,
            pomDurationInMin=5,
            pomBreakTimeInMin=1,
            pomReceiveFunction=PomBotReceive().getLastMessageIDTest,
            pomReactFunctionStart=PomBotReactEmojis().react_with_all_Test,
            pomReactFunctionEnd=PomBotReactEmojis().react_with_Numbers_Test,
        )
        return test_2_1_sparkle
