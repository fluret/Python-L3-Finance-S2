from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    moves = {
        "f": (0, 1),
        "b": (0, -1),
        "l": (-1, 0),
        "r": (1, 0),
    }

    if not instructions:
        return 0, 0

    x_steps, y_steps = zip(*(moves[step] for step in instructions))
    return sum(x_steps), sum(y_steps)