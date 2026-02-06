def yes_no(question):
    while True:
        response = input(f"{question}").lower()
        # check the user says yes/no
        if response == "yes" or response == "y":
            print("you said yes")
            return "yes"
        elif response == "no" or response == "n":
            print("you said no")
            return "no"
        else:
            print("please enter yes / no")

yes_no(" Insert question here ")
print(" insert end message here ")