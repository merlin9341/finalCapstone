
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.counrty = country
        self.code = code
        self.products = product
        self.cost = cost
        self.quantity = quantity
    def get_cost(self):
        "returns the cost of the shoes"
        return self.cost

    def get_quantity(self):
        "returns the quantity of the shoes in stock"
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.

        unsure what this means
        '''


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

    

    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
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