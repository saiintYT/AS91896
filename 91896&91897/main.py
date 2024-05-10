# functions within the code


# getting users budget


# getting users budget
def get_budget():
    
    
  while True:
      try:
          budget = float(input("What is your budget: "))
          if 1.65 <= budget <= 20:
              return budget
              
          elif budget < 1.65:
              print("Budget is too low. The minimum budget is 1.65.")
              
          else:
              print("Budget is too high. The maximum budget is 20.")
              
      except ValueError:
          print("Invalid input. Please enter a valid number.")


budget = get_budget()
print("Your budget is:", budget)


# getting users product name
def product_name(question):
    

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