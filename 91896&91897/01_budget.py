# getting users budget
def budget(question):


    while True:
        response = input(question)
        response = float(response)

        if response < 1.65:
            print("Your budget is too low, please enter a higher number.")

        elif response > 20:
            print("Your budget is too high, please enter a lower number.")

        elif response >= 1.65 or response <= 20:
            break

budget("What is your budget: ")