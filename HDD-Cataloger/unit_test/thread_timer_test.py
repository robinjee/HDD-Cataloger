import unittest
from unittest.mock import Mock
import sys 
sys.path.append('..')
from threadlib.timerthread import TimerThread

class Test_thread_timer_test(unittest.TestCase):

    def test_A(self):
        
        func = mock.Mock()
        tempTimer = TimerThread(130, func, 100, 0)
        tempTimer.start()
        expected = 5
        func.assert_called_with(5)

if __name__ == '__main__':
    unittest.main()
