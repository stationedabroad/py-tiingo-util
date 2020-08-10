import random
from typing import (
        Sequence, 
        TypeVar
        )


Choosable = TypeVar("Choosable")


def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)


names = ["Guido", "Jukka", "Ivan"]
reveal_type(names)

name = choose(names)
print(f" name is: {name} type is {reveal_type(name)}")

