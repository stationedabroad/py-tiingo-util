import time
import sentinel
from collections import OrderedDict
from datetime import timedelta

class TimeError(Exception):
    """ Custom exception for timer based exceptions """

class StopWatchTimerError(TimeError):
    """ Custom  exception for stopwatch based exceptions """

# Sentinels to use as default empty values
Nothing = sentinel.create('Nothing')
Empty = sentinel.create('Empty')

class StopWatchTimer:
    """ Stop Watch class which sort of mimics a stop watch (think apple iphone stop watch).
        With laps and reset
        Usage:
        At initialisation the timer starts, unless you pass defer=True, in which case an 
        instantiaited object exists to be started at your convenience with start()
    """
    def __init__(self, name: str = Empty, defer: bool = False):
        self.stopped_value = 0
        self.stopped = self.defer = defer
        if not self.defer:
            self.reset()
        self.name = name 

    def start(self):
        if self.stopped:
            self.start_count = time.perf_counter()
            self.stopped = self.defer = False            
        else:            
            self.reset()

    def stop(self):
        if self.stopped:
            raise StopWatchTimerError("StopWatchTimer already stopped, call start()")
        self.stopped_value = self.current()
        self.defer = self.stopped = True   

    def current(self) -> float:
        if not self.defer:
            return time.perf_counter() - self.start_count + self.stopped_value
        if self.stopped and self.stopped_value == 0:
            raise StopWatchTimerError("StopWatchTimer not started, call start()")
        return self.stopped_value

    def lap(self):
        lap_time = self.current()
        overall_dtime = str(timedelta(seconds=lap_time))
        self._laps[self._lap_number] = (overall_dtime, lap_time)
        self._lap_number += 1
        self._reset_lap()

    @property
    def laps(self):
        if not len(self._laps):
            print("No current laps")
            return
        for lap in self._laps.items():
            print(f"Lap: {lap[0]} -> {lap[1]}")

    def _reset_lap(self):
        self.start_time = time.time()
        self.start_count = time.perf_counter()   

    def reset(self):
        self.start_time = time.time()
        self.start_count = time.perf_counter()   
        self._lap_number = 0
        self._laps = OrderedDict()                 

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        if self.defer:
            return f"{class_name}(StopWatchTimer not started yet)"        
        begin = time.ctime(self.start_time)
        current_timer = self.current()
        return f"[{class_name}](Inception: {begin}, Current timer value: {str(timedelta(seconds=current_timer))})"



class Timer:
    """ Basic timer class to start and stop and return elpased time of code execution """
    def __init__(self):
        self._start_time = Nothing

    def start(self):
        if self._start_time is not None:
            raise TimeError(f"Timer in use, employ stop() method")
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimeError(f"Timer not started, use start()")
        elapsed = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed
