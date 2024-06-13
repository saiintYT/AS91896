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
