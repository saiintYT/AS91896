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


price = get_price()
print("Your price is:", price)
