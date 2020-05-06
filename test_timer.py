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
    assert timer._lap_number == some_laps
    assert len(timer._laps) == some_laps

def test_order_of_laps(some_laps):
    timer = Timer()
    for lap in range(some_laps):
        time.sleep(1)
        timer.lap()
    assert list(timer._laps.keys()) == [0, 1, 2]

def test_reset(some_laps):
    timer = Timer()
    st_count = timer.start_count
    for lap in range(some_laps):
        time.sleep(1)
        timer.lap()
    timer.reset()
    assert timer._lap_number == 0
    assert timer.start_count != st_count
    assert len(timer._laps ) == 0


