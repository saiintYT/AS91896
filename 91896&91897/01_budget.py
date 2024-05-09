#gettings users budget
def get_budget():
    
    
  while True:
      try:
          budget = float(input("What is your budget: "))
          if 1.65 <= budget <= 20:
              return budget
              
          elif budget < 1.65:
              print("Budget is too low. The Minimum budget is 1.65.")
              
          else:
              print("Budget is too high. The Maximum budget is 20.")
              
      except ValueError:
          print("Invalid input. Please enter a valid number.")


budget = get_budget()
print("Your budget is:", budget)
