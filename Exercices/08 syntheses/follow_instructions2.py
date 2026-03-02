from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    moves = {
        "f": (0, 1),
        "b": (0, -1),
        "l": (-1, 0),
        "r": (1, 0),
    }
    return (
        sum(moves[step][0] for step in instructions),
        sum(moves[step][1] for step in instructions),
    )