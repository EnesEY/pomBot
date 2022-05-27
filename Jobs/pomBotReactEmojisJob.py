import datetime
import time
from typing import Callable
import threading

class PomBotReactEmojisJob:
    def __init__(self, pomDurationInMin: int, pomBreakTimeInMin: int, pomReceiveFunction:Callable, pomReactFunction:Callable, pomStartMin:int):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.pomReceiveFunction = pomReceiveFunction
        self.pomReactFunction = pomReactFunction
        self.pomDurationInMin = pomDurationInMin
        self.pomBreakTimeInMin = pomBreakTimeInMin
        self.pomStartMin = pomStartMin

    def start_cycle(self):
        self._cycle_thread = threading.Thread(target=self._cycle)
        self.stop = False
        self._cycle_thread.start()

    def stop_cycle(self):
        self.stop = True
        self._cycle_thread.join()

    def _cycle(self):
        print('start cycle for react job')
        while not self.stop:
            now = datetime.datetime.now()
            if now.minute == self.pomStartMin:
                time.sleep(2)
                id = self.pomReceiveFunction()
                self.pomReactFunction(id)
                time.sleep((self.pomDurationInMin*60)-(60-now.second))
                time.sleep(2)
                id = self.pomReceiveFunction()
                self.pomReactFunction(id)
                time.sleep((self.pomBreakTimeInMin*60)-(60-now.second))
                self.pomStartMin = now.minute
            time.sleep(1)