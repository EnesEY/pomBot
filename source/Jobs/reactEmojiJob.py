import datetime
import time
import threading
from source.receiveMessage import ReceiveMessage
from source.reactWithEmoji import ReactWithEmoji


class ReactEmojiJob:
    def __init__(
        self,
        channel_string,
        pomStartMin,
        pomEndMin,
        pomDurationInMin,
        pomBreakTimeInMin,
    ):
        self._cycle_thread: threading.Thread = None
        self.stop: bool = False
        self.channel_string = channel_string
        self.pomReceiveFunction = (
            ReceiveMessage().get_last_bot_message_id_in_last_150_seconds
        )
        self.pomReactFunctionStart = ReactWithEmoji().react_with_all_sparkles
        self.pomReactFunctionEnd = ReactWithEmoji().react_with_all_numbers
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
        id = self.pomReceiveFunction(self.channel_string)
        if isStart == True:
            self.pomReactFunctionStart(id, self.channel_string)
            time.sleep((self.pomDurationInMin * 60) - (datetime.datetime.now().second))
        elif isStart == False:
            self.pomReactFunctionEnd(id, self.channel_string)
            time.sleep((self.pomBreakTimeInMin * 60) - (datetime.datetime.now().second))
