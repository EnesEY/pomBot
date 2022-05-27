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
            now = datetime.datetime.now()
            if now.minute == self.pomDoneMin:
                self.pomEndFunction()
                time.sleep((self.pomBreakTimeInMin*60))
                self.pomStartMin = now.minute
            if now.minute == self.pomStartMin:
                self.pomStartFunction()
                time.sleep(1.1)
                time.sleep((self.pomDurationInMin*60)-(now.second))
                self.pomEndFunction()
                time.sleep((self.pomBreakTimeInMin*60))
                self.pomStartMin = now.minute
                print(f'newPomStartTime:{self.pomStartMin}')
            time.sleep(1)

