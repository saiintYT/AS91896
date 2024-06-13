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


budget = get_budget()
print("Your budget is:", budget)

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


if __name__ == "__main__":
    main()

    


#def weight_g(question):
    # getting users weight in grams
#def weight_kg
#def cost
#def unit_price