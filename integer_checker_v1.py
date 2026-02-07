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
            
            
game_goal = int_check("What is the game goal?", 13)
print(f"Game goal: {game_goal}")
