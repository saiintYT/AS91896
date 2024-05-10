# getting users product name
def product_name(question):
    
    while True:

        response_pn = input(question)

        if response_pn.isalpha():
            input("Added, were there anymore? ")
        
            if response_pn.lower() == "yes" or response_pn.lower() == "y":
                return "yes"
        
        elif response_pn.lower() == "yes":
            print(product_name)
            
        elif response_pn.lower() == "no":
            print("All product names have been added.")
        
        else:
            print("Please only characters in the English alphabet.")

        if response_pn.lower() == "no" or response_pn.lower() == "n":
                return "no"

        

product_name("List your product's name: ")
