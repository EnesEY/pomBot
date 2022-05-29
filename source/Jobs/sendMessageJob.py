import datetime
import time
import threading
from Enums.pomBotEnums import ConfigEnum
from Configs.pom_config import PomConfig
from ..sendMessage import SendMessage


class SendMessageJob:
    def __init__(self, configEnum: ConfigEnum, pomStartMin, pomDoneMin):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.pomStartFunction = SendMessage().getSendMessageFunction(configEnum, True)
        self.pomEndFunction = SendMessage().getSendMessageFunction(configEnum, False)
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
        print("start cycle for send job")
        while not self.stop:
            if datetime.datetime.now().minute == self.pomDoneMin:
                self.send(False)
                self.pomStartMin = datetime.datetime.now().minute
                self.pomDoneMin = 999
            if datetime.datetime.now().minute == self.pomStartMin:
                self.send(True)
                self.send(False)
                self.pomStartMin = datetime.datetime.now().minute
            time.sleep(1)

    def send(self, isStart: bool):
        time.sleep(1)
        if isStart == True:
            self.pomStartFunction()
            time.sleep((self.pomDurationInMin * 60) - (datetime.datetime.now().second))
        elif isStart == False:
            self.pomEndFunction()
            time.sleep((self.pomBreakTimeInMin * 60) - (datetime.datetime.now().second))
