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