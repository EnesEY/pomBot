import datetime
import time
from typing import Callable
import threading


class PomBot:
    def __init__(self, pomStartFunction: Callable, pomEndFunction: Callable, pomDurationInMin: int, pomBreakTimeInMin: int):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.pomStartFunction = pomStartFunction
        self.pomEndFunction = pomEndFunction
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin

    def start_cycle(self):
        self._cycle_thread = threading.Thread(target=self._cycle)
        self.stop = False
        self._cycle_thread.start()

    def stop_cycle(self):
        self.stop = True
        self._cycle_thread.join()

    def _cycle(self):
        print('start cycle for pomBot')
        while not self.stop:
            now = datetime.datetime.now()
            if (now.minute % (self.pomDurationInMin + self.pomBreakTimeInMin)) == 0:
                self.pomStartFunction()
                time.sleep(self.pomDurationInMin*50)
            if (now.minute % self.pomDurationInMin) == 0:
                self.pomEndFunction()
                time.sleep(self.pomBreakTimeInMin*50)
            time.sleep(1)

