from random import random
from array import array
from typing import (
        Sequence, 
        TypeVar
        )


Choosable = TypeVar("Choosable", str, int)


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

more_names = ("Danny", "John", "Jules")
reveal_type(more_names)

set_more_names = set(["me", "you", "us", "me"])
reveal_type(set_more_names)

array_float = array('d', (random() for i in range(10)))
reveal_types(array_float)

name = choose(names)
reveal_type(names)

reveal_type([1,2,3])
reveal_type([True, False, True])
reveal_type([True, 0.21, 4.3])
reveal_type([4,5, "typing"])
reveal_type([False, False])
