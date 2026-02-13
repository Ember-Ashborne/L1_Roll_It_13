"""Minimal reusable dice function and tiny demo.

Function `roll_and_score` returns (d1, d2, total, is_double, points).
"""

import random


def roll_and_score(sides=6, double_multiplier=2):
    """Roll two dice and compute round points.

    Returns: (d1, d2, total, is_double, points)
    """
    d1 = random.randint(1, sides)
    d2 = random.randint(1, sides)
    total = d1 + d2
    is_double = d1 == d2
    points = total * (double_multiplier if is_double else 1)
    return d1, d2, total, is_double, points


if __name__ == "__main__":
    user = roll_and_score()
    comp = roll_and_score()

    sep = "=" * 40
    print(sep)
    print("YOU:   ", "Dice:", user[0], user[1], "Total:", user[2], "Points:", user[4])
    print("-" * 40)
    print("COMP:  ", "Dice:", comp[0], comp[1], "Total:", comp[2], "Points:", comp[4])
    print(sep)

    if user[4] > comp[4]:
        print("YOU WIN")
    elif user[4] < comp[4]:
        print("COMPUTER WINS")
    else:
        print("TIE")


        
