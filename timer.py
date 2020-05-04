import time
from collections import OrderedDict
from datetime import timedelta

class Timer:

    def __init__(self):
        self.reset()

    def current(self) -> float:
        return time.perf_counter() - self.start_count

    def lap(self):
        lap_time = self.current()
        overall_dtime = str(timedelta(seconds=lap_time))
        self._laps[self._lap_number] = (overall_dtime, lap_time)
        self._lap_number += 1
        self.reset_lap()

    @property
    def laps(self):
        if len(self._laps) == 0:
            print("No current laps")
        for lap in self._laps.items():
            print(f"Lap: {lap[0]} -> {lap[1]}")

    def reset_lap(self):
        self.start_time = time.time()
        self.start_count = time.perf_counter()   
        self._laps = OrderedDict()   

    def reset(self):
        self.start_time = time.time()
        self.start_count = time.perf_counter()   
        self._lap_number = 0
        self._laps = OrderedDict()                 

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        begin = time.ctime(self.start_time)
        current_timer = self.current()
        return f"{class_name}(Inception: {begin}, Current timer value: {str(timedelta(seconds=current_timer))})"
