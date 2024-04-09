# functions within the code


# getting users budget


def budget(question):


    while True:
        response = input('What is your budget: ')
        response = float(response)

        if response < 1.65:
            print("Your budget is too low, please enter a higher number.")

        elif response > 20:
            print("Your budget is too high, please enter a lower number.")

        elif response >= 1.65 or response <= 20:
            print("Please enter a valid number 1.65 - 20.")
            break

def product_name(question):
    # getting users product name

    response_pn = input("List your product's name: ")

    if response_pn == str:
        print("Added, were there anymore? ")

        if response_pn == "yes".lower or "y".lower:
            return "yes"
        
        elif response_pn == int:
            print("Please only characters in the english alphabet.")

        elif response_pn == "no".lower or "n".lower:
            return "no"

    if response_pn == "yes":
        print(product_name)


#def weight_g(question):
    # getting users weight in grams
#def weight_kg
#def cost
#def unit_price



# main routine

print("Hi")