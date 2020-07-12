import typing

def headline(text: str, centered: bool = False) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    return f" {text.title()} ".center(50, " ")

print(headline("some type checking"))
print(headline("some more type chekcing with mypy", centered=True))
