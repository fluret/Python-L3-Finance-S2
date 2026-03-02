from typing import Iterable

def remove_all_after(items: list, border: int) -> Iterable:
    if border in items:
        return items[:items.index(border) + 1]
    return items