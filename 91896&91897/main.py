"""This file calculates the most cost effective ingredient for them."""
# functions within the code
def budget(question):
    # getting users budget

    while True:
        response = input('What is your budget: ')
        response = float(response)

        if response < 1.65:
            print("Your budget is too low, please enter a higher number.")

        elif response > 5:
            print("Your budget is too high, please enter a lower number.")

        elif response >= 1.65 or response <= 5:
            continue

        else:
            print("Please enter a valid number 1.65 - 5.")

# main routine
