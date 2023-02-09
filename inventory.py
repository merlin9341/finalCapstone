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
        return self.quantity

    def get_product(self):
        "returns the name of the product"
        return self.product

    def get_code(self):
        return self.code
    
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
    "returns the details of the shoe with the lowest qunatity and askes if the user would like to add more"

    #uses min to find the smallest object in the list based on the __lt__ defined for Shoe
    lowest_shoe_index = shoe_list.index(min(shoe_list))

    #start a loop to ask the user what they would like to do with the item
    while True:
        restock_menu = input(f'''
Shoe with the lowest stock:   {shoe_list[lowest_shoe_index].get_product()}
stock remaining:              {shoe_list[lowest_shoe_index].get_quantity()}

Would you like to restock the item?(Y/N) > ''').lower()
        if restock_menu == "y":
            while True:
                try:
                    restock_menu_quantity = int(input("How many items would you like to restock? > "))

                    #use the restock method to update the value of the quantity for this instance of Shoe
                    shoe_list[lowest_shoe_index].restock(restock_menu_quantity)
                    print(f"\nThere are now {shoe_list[lowest_shoe_index].get_quantity()} of that shoe in stock")
                    break
                except ValueError:
                    print("\nPlease enter a valid quantity\n")
            break
        elif restock_menu == "n":
            break
        else:
            print("\nPlease enter Y or N")

def search_shoe():
    "allows the user to enter a code and display any shoes with matching codes from shoe_list"
    #Creates a list to hold codes
    #codes_list = [shoe.get_code() for shoe in shoe_list]
    codes_list = list(map(Shoe.get_code, shoe_list))

    #ask user to input code
    search_code = input("\nSEARCH > ")

    #chech if code is in list of codes
    if search_code in codes_list:
        
        #fetch the index of the code from code list to use to find shoe obect in shoe list to display
        found_shoe = shoe_list[codes_list.index(search_code)]

        #Use tabulate to print out shoe with headings
        print(tabulate([str(found_shoe).split(", ")], ["Quantity", "Product", "Product Code", "Country", "Price"]))
    else:
        print("\n--Sorry, code not found.--\n")

def value_per_item():
    "displays a table of the total value of each item = quanity * cost"
    #create a 2d list of each shoe name, product code and total value
    value_table =[[shoe.get_product(), shoe.get_code(), int(shoe.get_quantity()) * int(shoe.get_cost())] for shoe in shoe_list]

    #use tabulate to display data
    print(tabulate(value_table, ["Product", "Code", "Total Value"]))

def highest_qty():
    "Returns the deails of the shoe with the highest stock"

    #uses max to find the largest object in the list based on the __lt__ defined for Shoe
    highest_shoe_index = shoe_list.index(max(shoe_list))

    #uses tabulate to display this shoe 
    print("Shoe with highest stock:\n" + tabulate([str(shoe_list[highest_shoe_index]).split(", ")], ["Quantity", "Product", "Product Code", "Country", "Price"]))

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
rs - Restock shoe with lowest stock
sc - Search for a shoe by code
vi - Displays the total value per item in the stock list
hs - Displays the shoe with the highest stock
e - exit
> ''')
   
        if main_menu == "rd":
            read_shoes_data()
        elif main_menu == "ns":
            capture_shoes()
        elif main_menu == "va":
            view_all()
        elif main_menu == "rs":
            re_stock()
        elif main_menu == "sc":
            search_shoe()
        elif main_menu == "vi":
            value_per_item()
        elif main_menu == "hs":
            highest_qty()
        elif main_menu == "e":
            print("\nGoodbye!")
        else:
            print("\nPlease enter a valid input.")

main()