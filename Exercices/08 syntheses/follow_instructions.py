from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    moves = {
        "f": (0, 1),
        "b": (0, -1),
        "l": (-1, 0),
        "r": (1, 0),
    }

    x, y = 0, 0
    for step in instructions:
        dx, dy = moves[step]
        x += dx
        y += dy

    return x, y