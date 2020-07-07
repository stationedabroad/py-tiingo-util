from typing import Any, Callable, TypeVar, cast

FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)

def custom_decorator(f: F) -> F:
    """
        Takes a func, and returns a func - just like a decorator.
    """
    pass

for d in dir(custom_decorator):
    print(d)
print(custom_decorator.__annotations__)