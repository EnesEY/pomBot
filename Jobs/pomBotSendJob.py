import datetime
import time
import threading


class PomBotSendJob:
    def __init__(self, config, pomStartMin, pomDoneMin):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.pomStartFunction = config.pomStartFunction
        self.pomEndFunction = config.pomEndFunction
        self.pomDurationInMin = config.pomDurationInMin
        self.pomBreakTimeInMin = config.pomBreakTimeInMin
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
        print('start cycle for send job')
        while not self.stop:
            if datetime.datetime.now().minute == self.pomDoneMin:
                self.pomEndFunction()
                time.sleep((self.pomBreakTimeInMin*60) - (datetime.datetime.now().second))
                self.pomStartMin = datetime.datetime.now().minute
                self.pomDoneMin = 999
            if datetime.datetime.now().minute == self.pomStartMin:
                self.pomStartFunction()
                time.sleep((self.pomDurationInMin*60) - (datetime.datetime.now().second))
                self.pomEndFunction()
                time.sleep((self.pomBreakTimeInMin*60) - (datetime.datetime.now().second))
                self.pomStartMin = datetime.datetime.now().minute
                print(f'newPomStartTime:{self.pomStartMin}')
            time.sleep(1)

