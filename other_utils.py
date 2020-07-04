from typing import Any, Callable, TypeVar, cast

FuncType = Callable[..., Any]
F = TypeVar('F', bound=FuncType)

def custom_decorator(f: F) -> F:
    pass