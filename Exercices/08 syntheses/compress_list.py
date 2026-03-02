from typing import Iterable


def compress(items: list) -> Iterable:
    return [item for i, item in enumerate(items) if i == 0 or item != items[i - 1]]
