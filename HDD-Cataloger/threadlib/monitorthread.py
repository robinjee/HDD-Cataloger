from .basethread import BaseThread
from abc import ABCMeta, abstractmethod

class MonitorThread(BaseThread):
    def __init__(self):
        BaseThread.__init__(self)

    @abstractmethod
    def timerHandler(self, timerId):
        print("Monitor Thread Class")