# getting users cost of products
def get_price():
    
    
  while True:
      try:
          price = float(input("What is your price: "))
          if 1.65 <= price <= 20:
              return price
              
          elif budget < 1.65:
              print("Your price is too low. The minimum price is x.")
              
          else:
              print("Your price is too high. The maximum price is x.")
              
      except ValueError:
          print("Invalid input. Please enter a valid number.")


price = get_price()
print("Your budget is:", price)
