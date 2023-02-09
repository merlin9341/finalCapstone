#======Import Module========

from tabulate import tabulate

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
        self.quantity = int(quantity)
    def get_cost(self):
        "returns the cost of the shoes"
        return self.cost

    def get_quantity(self):
        "returns the quantity of the shoes in stock"
        return self.quantity#

    def get_product(self):
        "returns the name of the product"
        return self.get_product
    
    def restock(self, restock_quantity):
        self.quantity += restock_quantity

    def __str__(self):
        return f"{self.quantity}, {self.product}, {self.code}, {self.country}, {self.cost}"
    
    def __lt__(self, other):
        return self.quantity < other.quantity

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
    "Asks the user to enter the data for a show and then adds it to shoe_list as a Shoe object"
    #asks user to import required data, verifying that results that must be a integer are valid using try execpt blocks
    new_shoe_name = input("Product Name:\n> ")
    while True:
        new_shoe_code = input("Product code:\n> ")

        #ensure that code is 4 digits long
        if len(new_shoe_code) == 8:
            break
        else:
            print("\nPlease enter a 8 digit code\n")

    new_shoe_country = input("\nCountry of origin:\n> ")
    while True:
        try:
            new_shoe_cost = int(input("Unit cost:\n> "))
            break
        except ValueError:
            print("\nPlease enter a valid price\n")
    while True:
        try:
            new_shoe_quantity = int(input("Quantity:\n> "))
            break
        except ValueError:
            print("\nPlease enter a valid quantity\n")

    #create a new Shoe object 
    new_shoe = Shoe(new_shoe_country, new_shoe_code, new_shoe_name, new_shoe_cost, new_shoe_quantity)

    #save new shoe to shoe_list
    shoe_list.append(new_shoe)

    #print confirmation
    print("\n>>New shoe registered<<\n")
    
def view_all():
    "Prints the information held in the Shoe objects in shoe_list as a table"
    #checks if there are no shoes to display, if so displays an error and exits to main menu
    if shoe_list == []:
        print("\n--There are no products to display--")
        return

    #Begin a loop to interate over each Shoe object in the shoe list and add to a 2D list
    table_list = []
    for shoe in shoe_list:
        table_list.append(str(shoe).split(", "))

    #print to test
    print(tabulate(table_list, ["Quantity", "Product", "Product Code", "Country", "Price"]))

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
ns - input a new stock item
va - View all shoes
e - exit
> ''')
   
        if main_menu == "rd":
            read_shoes_data()
        elif main_menu == "ns":
            capture_shoes()
        elif main_menu == "va":
            view_all()
        elif main_menu == "e":
            print("\nGoodbye!")
        else:
            print("\nPlease enter a valid input.")

#main()

read_shoes_data()

print(shoe_list[0]< shoe_list[1])