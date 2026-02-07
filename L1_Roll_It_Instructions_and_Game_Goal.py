def yes_no(question):
    """Checks user response to a question for a yes/no answer and returns y/n."""
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

def instructions():
    """Prints instructions"""
    print("*** Instructions ***")
    print("Roll the dice and try to win!")
    
def int_check(question, low):
    error = f"Please enter an integer larger than or equal to {low}"

    while True:
        try:
            # Ask for a number with the custom prompt
            response = int(input(question))

            # Check if the number is valid
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
            



# Main routine

# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
print()

            
game_goal = int_check("What is the game goal? ", 13)
print(f"Game goal: {game_goal}")