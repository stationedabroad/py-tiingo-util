import os.path
import pytest
import time

from timer import Timer

@pytest.fixture
def some_laps(laps=3):
    return laps

def test_initialisation():
    timer = Timer()
    assert timer.start_time > 0 and type(timer.start_time) == float
    assert timer.start_count > 0 and type(timer.start_count) == float
    assert timer._lap_number == 0
    assert timer.laps == None

def test_laps(some_laps):
    timer = Timer()
    for lap in range(some_laps):
        time.sleep(1)
        timer.lap()
    print(timer.laps)
    assert timer._lap_number == some_laps
    assert len(timer._laps) == some_laps

def test_order_of_laps(some_laps):
    timer = Timer()
    for lap in range(some_laps):
        time.sleep(1)
        timer.lap()
    print(timer.laps)
    assert list(timer._laps.keys()) == [0, 1, 2]
