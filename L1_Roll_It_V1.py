# Import the random module so we can simulate dice rolls
import random


# Function to ask a yes/no question and ensure valid input
def yes_no(question):
    """Ask a yes/no question and return only 'yes' or 'no'."""
    
    while True:
        r = input(question).strip().lower()
        
        if r in ("yes", "y"):
            return "yes"
        elif r in ("no", "n"):
            return "no"
        else:
            print("Please enter yes / no")


# Function to print game instructions
def instructions():
    """Print the game instructions."""
    
    print("*** Instructions ***")
    print("1. Enter a game goal (minimum 13 points).")
    print("2. In Round 1, you and the computer roll TWO dice.")
    print("3. From Round 2 onwards, you both roll ONE die only.")
    print("4. If you roll a double in Round 1, your round points are doubled.")
    print("5. First to reach or pass the game goal wins.")
    print("6. If both players reach the goal in the same round, the one with more points wins.")


# Function to check for a valid integer above a minimum value
def int_check(question, low):
    """Ask for an integer >= low."""
    
    err = f"Please enter an integer larger than or equal to {low}"
    
    while True:
        try:
            val = int(input(question))
            
            if val >= low:
                return val
            else:
                print(err)
        
        except ValueError:
            print(err)


# Function to roll two dice
def roll_two_dice(sides=6, double_multiplier=2):
    d1 = random.randint(1, sides)
    d2 = random.randint(1, sides)
    
    total = d1 + d2
    is_double = d1 == d2
    
    if is_double:
        points = total * double_multiplier
    else:
        points = total
    
    return d1, d2, total, is_double, points


# Function to roll one die
def roll_one_die(sides=6):
    d1 = random.randint(1, sides)
    return d1


# MAIN ROUTINE STARTS HERE

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
    
    sep = "=" * 40
    print(sep)
    print(f"ROUND {round_num}")
    
    # ROUND 1 → TWO DICE
    if round_num == 1:
        
        user_d1, user_d2, user_total, user_is_double, user_round_points = roll_two_dice()
        comp_d1, comp_d2, comp_total, comp_is_double, comp_round_points = roll_two_dice()
        
        user_points += user_round_points
        comp_points += comp_round_points
        
        print("YOU:  Dice:", user_d1, user_d2,
              "Total:", user_total,
              "Points:", user_round_points,
              "Score:", user_points)
        
        if user_is_double:
            print(">> NICE! You rolled a double, so your points were doubled!")
        
        print("-" * 40)
        
        print("COMP: Dice:", comp_d1, comp_d2,
              "Total:", comp_total,
              "Points:", comp_round_points,
              "Score:", comp_points)
        
        if comp_is_double:
            print(">> Computer rolled a double, so its points were doubled!")
    
    # ROUND 2+ → ONE DIE
    else:
        
        user_roll = roll_one_die()
        comp_roll = roll_one_die()
        
        user_points += user_roll
        comp_points += comp_roll
        
        print("YOU:  Roll:", user_roll,
              "Points:", user_roll,
              "Score:", user_points)
        
        print("-" * 40)
        
        print("COMP: Roll:", comp_roll,
              "Points:", comp_roll,
              "Score:", comp_points)
    
    print(sep)
    
    round_num += 1


if user_points > comp_points:
    print("\nYOU WIN")
elif user_points < comp_points:
    print("\nCOMPUTER WINS")
else:
    print("\nTIE")
