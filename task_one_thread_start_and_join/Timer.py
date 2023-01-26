"""
A class that starts a timer on initialization before the method one wants to time
Then it can be stopped at the end of the test that one wants to time
"""
import time


class Timer(object):

    def __init__(self) -> None:
        self.start = time.perf_counter()

    def stop(self):
        finish = time.perf_counter()
        print(f'Finished in {round(finish - self.start, 2)} second(s)')
