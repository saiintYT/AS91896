def get_product_name():
    while True:
        product_name = input("Enter the product name: ").strip()
        if product_name:
            if all(char.isalpha() or char.isspace() for char in product_name):
                return product_name
            else:
                print(
                    "Invalid input. Please use only English alphabet letters and spaces."
                )
        else:
            print("Product name cannot be empty.")


def main():
    products = []
    while True:
        product = get_product_name()
        if product:
            products.append(product)
            while True:
                choice = input(
                    "Do you want to add more products? (yes/no): ").lower()
                if choice == 'yes' or choice == 'y':
                    break
                elif choice == 'no' or choice == 'n':
                    print("All product names have been added.")
                    print("List of products:")
                    print("\n".join(products))
                    exit()

                else:
                    print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()

    