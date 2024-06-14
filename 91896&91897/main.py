# functions within the code


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




# getting users product name
def get_product_name():
  while True:
      product_name = input("Enter the product name: ")
      if product_name.isalpha():
              return product_name
      else:
              print("Invalid input. Please use only English alphabet letters and spaces.")
          
def main():
  products = []
  while True:
      product = get_product_name()
      if product:
          products.append(product)
          while True:
              choice = input("Do you want to add more products? (yes/no): ").lower()
              if choice == 'yes' or choice == 'y':
                  break  # Exit the inner loop to continue adding products
              elif choice == 'no' or choice == 'n':
                  print("All product names have been added.")
                  print("List of products:")
                  print("\n".join(products))
                  return  # Exit the main function, effectively ending the program
              else:
                  print("Please enter 'yes' or 'no'.")


def get_weight():
# getting users weight


  while True:
      try:
          weight = float(input("What is your weight(in kg): "))
          if 0 <= weight <= 50:
              return weight
              
          elif weight <= 0:
              print("Weight is too low. The minimum weight is 1.")
              
          else:
              print("Weight is too high. The maximum weight you can enter is 50.")
              
      except ValueError:
          print("Invalid input. Please enter a valid number.")


weight = get_weight()
print("The weight of {product_name} is:", weight)

# getting users cost of products
def get_price():
    
    
  while True:
      try:
          price = float(input("What is your price: "))
          if 0 <= price <= 2000:
              return price
              
          elif price < 0:
              print("Your price is too low. The minimum price is x.")
              
          else:
              print("Your price is too high. The maximum price is x.")
              
      except ValueError:
          print("Invalid input. Please enter a valid number.")



# Main routine goes here
budget = get_budget()
print("Your budget is:", budget)

product = get_product_name()
print("Your product is:", product)

weight = get_weight()
print("The weight of {product_name} is:", weight)

price = get_price()
print("Your price is:", price)

if __name__ == "__main__":
    main()