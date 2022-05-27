from typing import Callable
from pomBotSendMessage import PomBotSend
from pomBotReceiveMessage import PomBotReceive
from pomBotReactEmojis import PomBotReactEmojis

class PomConfig():
    def __init__(self,pomStartFunction: Callable, pomEndFunction: Callable, pomDurationInMin: int, pomBreakTimeInMin: int, pomReceiveFunction:Callable, pomReactFunction:Callable):
        self.pomStartFunction = pomStartFunction
        self.pomEndFunction = pomEndFunction
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.pomReceiveFunction = pomReceiveFunction
        self.pomReactFunction = pomReactFunction

        self.pomBotSend = PomBotSend()
        self.pomBotReceive = PomBotReceive()
        self.pomBotReact = PomBotReactEmojis()

    mowgli_25_5_sparkle = PomConfig(
        pomStartFunction=pomBotSend.startEmojiToMogli,
        pomEndFunction=pomBotSend.doneEmojiToMogli,
        pomDurationInMin=25,
        pomBreakTimeInMin=5,
        pomReceiveFunction=pomBotReceive.getLastMessageIDMogli,
        pomReactFunction=pomBotReact.react_with_all_mogli
    )

    test_2_1_sparkle = PomConfig(
        pomStartFunction=pomBotSend.startEmojiToTest,
        pomEndFunction=pomBotSend.doneEmojiToTest,
        pomDurationInMin=2,
        pomBreakTimeInMin=1,
        pomReceiveFunction=pomBotReceive.getLastMessageIDTest,
        pomReactFunction=pomBotReact.react_with_all_Test
    )


