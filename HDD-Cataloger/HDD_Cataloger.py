from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import os
from gui_layer.design import Ui_MainWindow
from multiprocessing  import Queue
import struct
from threadlib.monitorthread import MonitorThread

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # gui_queue gui is the owner and reads on it
        gui_queue = Queue(maxsize=0)
        # logic layer is the owner to read
        logic_queue = Queue(maxsize=0)
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self, gui_queue)

class MyThread(MonitorThread):
    def __init__(self):
        MonitorThread.__init__(self)
        self.createTimer(100, 1000, 1000)
        self.startTimer(100)
        self.createTimer(100, 100, 100)
        self.startTimer(100)

    def timerHandler(self, timerId):
        print("timer call with timer Id ", timerId)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    thread1 = MyThread()
    app.exec_()


if __name__ == '__main__':
    main()