# functions
def budget(question):

    while True:
        response = int(input('Budget: '))
        
        if response < 1.65:
            print("Your budget is too low, please enter a higher number.")
                
        elif response > 5:
            print("Your budget is too high, please enter a lower number.")

        elif response >= 1.65 or response <= 5:
            continue

        else:
            print("Please enter a valid number 1.65 - 5.")


# main routine

# getting users budget
while True:
    question = budget("Budget: ")

    if budget == 1.65 to 5:
