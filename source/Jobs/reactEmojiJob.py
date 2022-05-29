import datetime
import time
import threading
from Enums.PomBotEnums import ConfigEnum
from Configs.pom_config import PomConfig
from ..receiveMessage import ReceiveMessage
from ..reactWithEmoji import ReactWithEmoji


class ReactEmojiJob:
    def __init__(self, configEnum: ConfigEnum, pomStartMin, pomDoneMin):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.pomReceiveFunction = ReceiveMessage().getReceiveFunction(configEnum)
        self.pomReactFunctionStart = ReactWithEmoji().getReactWithEmojiFunction(configEnum, True)
        self.pomReactFunctionEnd = ReactWithEmoji().getReactWithEmojiFunction(configEnum, False)
        self.pomDurationInMin = PomConfig(configEnum).pomDurationInMin
        self.pomBreakTimeInMin = PomConfig(configEnum).pomBreakTimeInMin
        self.pomStartMin = pomStartMin
        self.pomDoneMin = pomDoneMin

    def start_cycle(self):
        self._cycle_thread = threading.Thread(target=self._cycle)
        self.stop = False
        self._cycle_thread.start()

    def stop_cycle(self):
        self.stop = True
        self._cycle_thread.join()

    def _cycle(self):
        print("start cycle for react job")
        while not self.stop:
            if datetime.datetime.now().minute == self.pomDoneMin:
                self.react(False)
                self.pomStartMin = datetime.datetime.now().minute
                self.pomDoneMin = 999
            if datetime.datetime.now().minute == self.pomStartMin:
                self.react(True)
                self.react(False)
                self.pomStartMin = datetime.datetime.now().minute
                print(f"newPomStartTime:{self.pomStartMin}")
            time.sleep(1)

    def react(self, isStart: bool):
        time.sleep(2)
        id = self.pomReceiveFunction()
        if isStart == True:
            self.pomReactFunctionStart(id)
            time.sleep((self.pomDurationInMin * 60) - (datetime.datetime.now().second))
        elif isStart == False:
            self.pomReactFunctionEnd(id)
            time.sleep((self.pomBreakTimeInMin * 60) - (datetime.datetime.now().second))
