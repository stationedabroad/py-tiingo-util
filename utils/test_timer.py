import os.path
import pytest
import time

from .timer import (
    Timer, 
    StopWatchTimer, 
    StopWatchTimerError
)

LAPS = 3

@pytest.fixture
def some_laps(laps=LAPS):
    return laps

@pytest.fixture
def timer_obj(some_laps):
    t = StopWatchTimer()
    for _ in range(some_laps):
        time.sleep(1)
        t.lap()
    return t

@pytest.fixture
def deferred_timer():
    t = StopWatchTimer(defer=True)
    return t

def test_timer_start():
    timer = StopWatchTimer()
    assert timer.start_time > 0 and type(timer.start_time) == float
    assert timer.start_count > 0 and type(timer.start_count) == float
    assert timer._lap_number == 0
    assert timer.laps == None

def test_timer_stop():
    timer = StopWatchTimer()
    time.sleep(1)
    timer.stop()
    time.sleep(2)
    # stop timer then check
    assert round(timer.current()) == 1
    # start and stop then check
    timer.start()
    time.sleep(2)
    timer.stop()
    time.sleep(1)
    assert round(timer.current()) == 3


def test_laps(timer_obj, some_laps):
    timer = timer_obj
    assert timer._lap_number == some_laps
    assert len(timer._laps) == some_laps

def test_order_of_laps(timer_obj):
    timer = timer_obj
    assert list(timer._laps.keys()) == [0, 1, 2]

def test_reset(timer_obj):
    timer = timer_obj
    st_count = timer.start_count
    timer.reset()
    assert timer._lap_number == 0
    assert timer.start_count != st_count
    assert len(timer._laps ) == 0

def test_current_on_deferred_start(deferred_timer):
    """ check current timer on a deferred start stopWatch, should raise custom error """
    timer = deferred_timer
    with pytest.raises(StopWatchTimerError):
        timer.current()

def test_stop_when_already_stopped(deferred_timer):
    """ stop a stop watched when already stopped, should raise custom error """
    timer = deferred_timer
    with pytest.raises(StopWatchTimerError):
        timer.stop()