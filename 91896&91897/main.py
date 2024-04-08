"""This file calculates the most cost effective ingredient for them."""
# functions within the code
def budget(question):
# getting users budget

    while True:
        response = input('What is your budget: ')
        response = float(response)

        if response < 1.65:
            print("Your budget is too low, please enter a higher number.")

        elif response > 20:
            print("Your budget is too high, please enter a lower number.")

        elif response >= 1.65 or response <= 20:
            continue

        else:
            print("Please enter a valid number 1.65 - 20.")
            
def product_name(question):
    # getting users product name

    response_pn = input("List your product's name: ")

    if response_pn == str:
        print("Added, were there anymore? ")

        if response_pn == "yes".lower or "y".lower:
    elif response_pn == int:
        print("Please only characters in the english alphabet.")

def weight_g(question):
    # gettins users weight in grams
def weight_kg
def cost
def unit_price

 

# main routine

print(" ")