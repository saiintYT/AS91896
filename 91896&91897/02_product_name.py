def product_name(question):
    # getting users product name

    response_pn = input(question)

    if response_pn == str:
        print("Added, were there anymore? ")

        if response_pn == "yes".lower or "y".lower:
                return "yes"
        
    elif response_pn == int:
            print("Please only characters in the english alphabet.")

            if response_pn == "no".lower or "n".lower:
                return "no"

    if response_pn == "yes":
        print(product_name)

product_name("List your product's name: ")