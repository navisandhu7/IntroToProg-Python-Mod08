# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# NSandhu,06.05.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import sys
import pickle

# Data -------------------------------------------------------------------- #
strFileName = 'products.dat'
lstOfProductObjects = []
userChoice = ""
userAdd = None
userRemove = ""

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NSandhu,06.05.2022,Modified code to complete assignment 8
    """

    # -- Constructor -- #
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties -- #
    # Product Name
    @property
    def product_name(self):
        if str(self.__product_name_str).isalpha():
            return str(self.__product_name_str).title()
        else:
            return self.__product_name_str

    @product_name.setter
    def product_name(self, data):
        try:
            if not str(data).isnumeric():
                self.__product_name_str = data
            else:
                raise Exception("Product names cannot contain numbers!")
        except Exception as e1:
            IO.error_message(e1)
            self.__product_name_str = None

    # Product Price
    @property
    def product_price(self):
        if str(self.__product_price_val).isnumeric():
            return float(self.__product_price_val)
        else:
            return self.__product_price_val

    @product_price.setter
    def product_price(self, data):
        try:
            if not str(data).isalpha():
                self.__product_price_val = data
            else:
                 raise Exception("Product prices cannot contain non-numeric characters!")
        except Exception as e2:
            IO.error_message(e2)
            self.__product_price_val = None


# -- End of Class -- #

# End of Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> binary file with product/price data

        read_data_from_file(file_name): -> (a list of product objects)

        remove_product(name,data): -> list of product objects with user input removed if found

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        NSandhu,06.05.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name="products.dat", list_of_product_objects=[]):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file, default is products.dat:
        :param list_of_product_objects: (list) you want filled with file data, default is blank:
        :return: nothing
        """
        file = open(file_name, "wb")
        pickle.dump(list_of_product_objects, file)
        file.close()
        print("Data saved!")

    @staticmethod
    def read_data_from_file(file_name="products.dat"):
        """ Reads in existing pickled data, else creates new pickle file

        :param file_name: file where stored schedule data is, default is products.dat. Note that this file needs to
        exist prior to code execution:
        :return: data
        """
        data = []
        try:
            file = open(file_name, "rb")
            while True:
                try:
                    data = pickle.load(file)
                except EOFError as e:
                    IO.error_message(e)
                    break
        except FileNotFoundError as e:
            IO.error_message(e)
        file.close()
        return data

    @staticmethod
    def remove_product(name, data):
        """ Removes data from a list of product objects

        :param event: (string) with name of event to remove:
        :param data: (list) filled with schedule data:
        :return: (list) of dictionary rows of schedule data
        """
        i = 0
        flag = 0
        for row in data:
            if row.product_name.lower() == name.lower().strip():
                flag = 1
                i += 1
                data.remove(row)
                print("Product removed from list.")
            else:
                i += 1
                if i == len(data) and flag == 0:
                    print("Product not found.")
                    print()  # print new line for looks
        return data


# End of Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input/Output tasks, presenting and retrieving outputs and inputs for/from the user:

    methods:
        welcome_message(): -> welcome message to user

        display_menu(): -> menu display to user

        get_menu_input(): -> user input for menu option desired

        error_message(error): -> error information displayed to user

        view_list(data): -> current list of product information displayed to user

        get_user_product_info(): -> Product object with (obj).product_name and (obj).product_price info

        get_user_product_to_remove(): -> string from user input for product to remove from list

        exit_message(): -> exit message displayed to user

    changelog: (When,Who,What)
        NSandhu,06.05.2022,Created class and added necessary methods for Assignment08
    """
    @staticmethod
    def welcome_message():
        """  Display a Welcome message to the user

        :return: nothing
        """

        print("""
        Welcome to the Product Pricer! I will help you
        create and manage a list of product items and their prices.
        Please choose from a menu option to get started:
        """)

    @staticmethod
    def display_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''\n
        Menu of Options
        1) View current Product List
        2) Add a new Product and Price to the List
        3) Remove a Product from the List
        4) Save the List
        5) Exit Program
        ''')
        print()

    @staticmethod
    def get_menu_input():
        """  Get user input for any item

         :return: choice
            """
        choice = input("Please select a menu option from 1-5: ").strip()
        return choice

    @staticmethod
    def error_message(error):
        """  Displays one of several error messages based on exception raised

        :param error: an exception object:
        :return: nothing
        """
        print()
        if isinstance(error, ValueError):
            print("Please only enter integer values!\n")
        elif isinstance(error, EOFError):
            pass
        elif isinstance(error, FileNotFoundError):
            sys.exit("Product file does not exist, please create a blank 'products.dat' file in the local directory "
                  "and try again")
        elif isinstance(error, Exception):
            print(error)

    @staticmethod
    def view_list(data):
        """ Shows the current list of products and prices

                :param data: list of data to be displayed:
                :return: nothing
                """
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("The Product List is: ")
        for row in data:
            print(row.product_name,str(row.product_price),sep="\t||\t")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print()

    @staticmethod
    def get_user_product_info():
        """
        Returns user product and pricing information

        :param: none
        :return product_obj: -> Product object instance with (obj).product_name and (obj).product_price info
        :return e: -> error information
        """
        user_product_name = input("Please enter Product Name (non-numeric only): ")
        user_product_price = input("Please enter Product Price (numeric only): ")
        product_obj = Product(user_product_name,user_product_price)
        return product_obj

    @staticmethod
    def get_user_product_to_remove():
        """
        Get user input for product to remove from list

        :param: none
        :return remove_product: string from user for product to remove
        """
        remove_product = input("Please input product name to remove: ").strip()
        return remove_product

    @staticmethod
    def exit_message():
        """  Displays a message to the user prior to exiting program

        :return: nothing
        """
        print("Thank you! Program will end upon hitting 'Enter'...")
# End of Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

IO.welcome_message()

while True:
    IO.display_menu()
    try:
        userChoice = int(IO.get_menu_input())
        if userChoice not in range(1,6):
            raise Exception("Please only input a value from 1 to 5!")
    except ValueError as e:
        IO.error_message(e)
        continue
    except Exception as e:
        IO.error_message(e)
        continue

    match userChoice:
        case 1:
            IO.view_list(lstOfProductObjects)
        case 2:
            userAdd = IO.get_user_product_info()
            if userAdd.product_name == 'None':
                continue
            elif userAdd.product_price is None:
                continue
            else:
                lstOfProductObjects.append(userAdd)
        case 3:
            userRemove = IO.get_user_product_to_remove()
            lstOfProductObjects = FileProcessor.remove_product(userRemove,lstOfProductObjects)
        case 4:
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        case 5:
            IO.exit_message()
            input()
            break

# End Main  ---------------------------------------------------- #
