from typing import Iterable


def compress(items: list) -> Iterable:
    result = []
    for val in items:
        if result:
            if val != result[-1]:
                result.append(val)
        else:
            result.append(val)
    return result