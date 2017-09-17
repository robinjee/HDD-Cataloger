from PyQt5 import QtCore, QtGui, QtWidgets

class Register_UI_Events(object): 
    __instance = None

    def __init__(self):
        import sys
        if Register_UI_Events.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            self.observers = []
 
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Register_UI_Events.__instance == None:
            Register_UI_Events()
        return Register_UI_Events.__instance 

    def addEvents():
        pass

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
 
    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
 
    def unregister_all(self):
        if self.observers:
            del self.observers[:]
 
    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)