from typing import List


def fit(lst: List, a, b) -> None:
    if b < a:
        raise ValueError("b must be greater or equals a")

    for i, x in enumerate(lst):
        if x < a:
            lst[i] = a
        elif x > b:
            lst[i] = b
