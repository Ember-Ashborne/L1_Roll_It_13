"""
Beginner-friendly one-round script for the "Roll It" dice game.

This version follows the simple steps from the screenshot with
clear comments and straightforward, linear code so beginners can
follow each step easily.
"""
import random

# Initialise rounds points
user_points = 0
computer_points = 0

# Roll the dice for the user and note if they got a double
u1 = random.randint(1, 6)
u2 = random.randint(1, 6)
user_total = u1 + u2
user_double = (u1 == u2)

# roll the dice for the computer
c1 = random.randint(1, 6)
c2 = random.randint(1, 6)
comp_total = c1 + c2
comp_double = (c1 == c2)

# Update the user / computer points
if user_double:
    # Double the points when both dice are the same
    user_points += user_total * 2
else:
    user_points += user_total

if comp_double:
    computer_points += comp_total * 2
else:
    computer_points += comp_total

# Output the results with decoration (beginner-friendly)
sep = "=" * 40
print(sep)
print("\t   ROLL IT — ROUND RESULTS")
print(sep)

print("YOU:")
print(f"  Dice: {u1} and {u2}")
print(f"  Total: {user_total}")
if user_double:
    print("  >> DOUBLE! Round points are doubled <<")
print(f"  Round points: {user_points}")

print("-" * 40)

print("COMPUTER:")
print(f"  Dice: {c1} and {c2}")
print(f"  Total: {comp_total}")
if comp_double:
    print("  >> DOUBLE! Round points are doubled <<")
print(f"  Round points: {computer_points}")

print(sep)
# Announce winner for the round inside a small box
if user_points > computer_points:
    result = "YOU WIN THIS ROUND!"
elif user_points < computer_points:
    result = "COMPUTER WINS THIS ROUND"
else:
    result = "THIS ROUND IS A TIE"

box = f"***  {result}  ***"
print(box.center(40))
print(sep)
