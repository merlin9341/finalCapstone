#======Define Constants======
COUNTRY = 0
CODE = 1
PRODUCT = 2
COST = 3
QUANTITY = 4

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    def get_cost(self):
        "returns the cost of the shoes"
        return self.cost

    def get_quantity(self):
        "returns the quantity of the shoes in stock"
        return self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product} ({self.code}) from {self.country} - £{self.cost}"

#=============Shoe list===========

#A list used to store the shoe objects
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    "Reads data from the file inventory.txt and saves it in the inventory list. If the file is not present the function prints an error message."
    
    #A try except block is used to check for the presence of the inventory file
    try:
        open("inventory.txt", "r")
    except FileNotFoundError:
        print("Sorry, inventory file not found, please create it.")
        return

    #Open the file using with and as
    with open("inventory.txt", "r") as inventory_file:
        
        #use readline to move the marker to after the title line
        inventory_file.readline()

        #start a loop to read through the remaining lines:
        for line in inventory_file:
            paramaters_list = line.strip("\n").split(",")
            
            #create a new instance of the shoe object with the atributes from the list
            new_shoe = Shoe(
                paramaters_list[COUNTRY], 
                paramaters_list[CODE], 
                paramaters_list[PRODUCT],
                paramaters_list[COST],
                paramaters_list[QUANTITY]
                )
            
            #add the new show object to the list that holds the shoes
            shoe_list.append(new_shoe)
    
    #Print confirmation message
    print("\n--Data read from file--\n")

def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
def main():
    "Main menu loop"

    main_menu = ""
    while main_menu != "e":
        main_menu = input('''
---Main menu---

Please select one of the following options:
rd - read inventory data from file
e - exit
> ''')
   
        if main_menu == "rd":
            read_shoes_data()
        elif main_menu == "e":
            print("\nGoodbye!")
        else:
            print("\nPlease enter a valid input.")

main()