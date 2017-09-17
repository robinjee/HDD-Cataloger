from threading import Thread
from .timerthread import TimerThread
from .constants import CONSTANTS
from abc import ABCMeta, abstractmethod

class BaseThread(Thread):
    """
    BaseThread class : abstract class for threading wit in built signal, timer and queue handler
    """
    @abstractmethod
    def __init__(self):
        """
        constructor : initialses ipc lists
        """
        Thread.__init__(self)
        self.daemon = True
        self.timerList = {}
        self.threadQueuelist = {}

    def createTimer(self, timerId, onceMS, periodicMS ):
        """
        createTimer : create instance of a timer thread with the baseTimerHandler as call back method
        timerId : timer id to recognise while call back
        onceMS : for 1 time call back
        periodicMS : for periodic call back
        """
        if not timerId in self.timerList.keys():
            tempTimer = TimerThread(timerId, self.baseTimerHandler, onceMS, periodicMS)
            self.timerList.setdefault(timerId, tempTimer)
        

    def startTimer(self, timerId):
        """
        startTimer : starts the timer thread with particuar timerId
        """
        tempTimer = self.timerList.setdefault(timerId)
        tempTimer.start()

    def run(self):
        """
        run : starts the thread
        """
        pass

    def baseTimerHandler(self, timerId):
        """
        baseTimerHandler : timer handler method
        timerId : if timerId is 100 or above then forwards to userdefined call back
        """
        if timerId > CONSTANTS.TIMER_ID_RESERVED :
            self.timerHandler(timerId)

    @abstractmethod
    def timerHandler(self, timerId):
        """
        timerHandler : abstract method for user defined timer handler
        """
        print("Base Thread Class")
        

    def queueHandler(self):
        """
        queueHandler : abstract method for user defined queue handler
        """
        pass

    def signalhandler(signum, frame):
        """
        signalhandler : abstract method for user defined signal handler
        """
        pass