from threading import Timer,Thread,Event

class TimerThread():
   """
   TimerThread class : Its a threaded timer class with user defined call back
   """
   def __init__(self, timerId, hFunction, onceTime=0, periodicTime=0):
      """
      timer thread constructor
      timerId : user defined timers should be above 99, 3 digits and above
      hFunction : user defined call back function
      onceTime : if one time timer needed
      periodicTime : if periodic timer needed
      """
      self.timerId = timerId
      self.onceTime = onceTime / 1000.0
      self.periodicTime = periodicTime / 1000.0
      self.hFunction = hFunction
      self.thread = Timer(self.onceTime, self.handle_function)
    
   def handle_function(self):
      """
      Its the initial call back function before forwarding to user defined call back function
      if timer is a periodic timer it resets the timer
      """
      self.hFunction(self.timerId)
      if self.periodicTime == 0:
          self.cancel()
          return
      self.thread = Timer(self.periodicTime, self.handle_function)    
      self.thread.daemon = True
      self.thread.start()

   def start(self):
       """
       starts the timer thread
       """
       if not self.thread.is_alive():
           self.thread.start()

   def cancel(self):
      """
      stops the timer thread
      """
      self.thread.cancel()