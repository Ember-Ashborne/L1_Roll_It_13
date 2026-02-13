# functions go here
def yes_no(question):
    """Checks user response to a question for a yes/no answer and returns y/n."""
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""
    print("*** Instructions ***")
    print("Roll the dice and try to win!")

# Main routine
# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions? ")
# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
print()
print("Program continues")