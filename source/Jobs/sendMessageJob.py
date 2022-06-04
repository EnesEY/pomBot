import datetime
import time
import threading
from source.sendMessage import SendMessage


class SendMessageJob:
    def __init__(self, channel_string, pomStartMin, pomEndMin, pomDurationInMin, pomBreakTimeInMin):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.channel_string = channel_string
        self.pomStartFunction = SendMessage().sendStartMessage
        self.pomEndFunction = SendMessage().sendEndMessage
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.pomStartMin = pomStartMin
        self.pomDoneMin = pomEndMin

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
            self.pomStartFunction(self.channel_string)
            time.sleep((self.pomDurationInMin * 60) - (datetime.datetime.now().second))
        elif isStart == False:
            self.pomEndFunction(self.channel_string)
            time.sleep((self.pomBreakTimeInMin * 60) - (datetime.datetime.now().second))
