import random


def yes_no(question):
    """Ask a yes/no question; return 'yes' or 'no'."""
    while True:
        r = input(question).strip().lower()
        if r in ("yes", "y"):
            return "yes"
        if r in ("no", "n"):
            return "no"
        print("Please enter yes / no")


def instructions():
    print("*** Instructions ***")
    print("1. Enter a game goal (minimum 13 points).")
    print("2. Each round, you and the computer roll two dice.")
    print("3. Your round points are the sum of both dice.")
    print("4. If you roll a double, your round points are doubled.")
    print("5. First to reach or pass the game goal wins.")
    print("6. If both players reach the goal in the same round, the one with more points wins.")


def int_check(question, low):
    """Ask for an integer >= low."""
    err = f"Please enter an integer larger than or equal to {low}"
    while True:
        try:
            val = int(input(question))
            if val >= low:
                return val
            print(err)
        except ValueError:
            print(err)


def roll_and_score(sides=6, double_multiplier=2):
    """Roll two dice and return (d1, d2, total, is_double, points)."""
    d1 = random.randint(1, sides)
    d2 = random.randint(1, sides)
    total = d1 + d2
    is_double = d1 == d2
    points = total * (double_multiplier if is_double else 1)
    return d1, d2, total, is_double, points


if __name__ == "__main__":
    if yes_no("Do you want to see the instructions? ") == "yes":
        instructions()
    print()

    goal = int_check("What is the game goal? ", 13)
    print(f"Game goal: {goal}")

    user_points = 0
    comp_points = 0
    round_num = 1

    while user_points < goal and comp_points < goal:
        input(f"\nPress Enter to play round {round_num}...")

        user = roll_and_score()
        comp = roll_and_score()

        user_points += user[4]
        comp_points += comp[4]

        sep = "=" * 40
        print(sep)
        print(f"ROUND {round_num}")
        print("YOU:  Dice:", user[0], user[1], "Total:", user[2], "Points:", user[4], "Score:", user_points)
        if user[3]:
            print(">> NICE! You rolled a double, so your points were doubled!")
        print("-" * 40)
        print("COMP: Dice:", comp[0], comp[1], "Total:", comp[2], "Points:", comp[4], "Score:", comp_points)
        if comp[3]:
            print(">> Computer rolled a double, so its points were doubled!")
        print(sep)

        round_num += 1

    if user_points > comp_points:
        print("\nYOU WIN")
    elif user_points < comp_points:
        print("\nCOMPUTER WINS")
    else:
        print("\nTIE")
