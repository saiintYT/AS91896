def product_name(question):
    # getting users product name

    while True:

        response_pn = input(question)

        if response_pn.isalpha():
            print("Added, were there anymore? ")

            if response_pn.lower() == "yes" or response_pn.lower() == "y":
                return "yes"
            
        else:
            print("Please only characters in the English alphabet.")

            if response_pn.lower() == "no" or response_pn.lower() == "n":
                return "no"

        if response_pn.lower() == "yes":
            print(product_name)

product_name("List your product's name: ")
