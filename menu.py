import string
import random
import sys
import generator
import csv_operations

def take_passwordgen_input():
    custom_flag = False

    # Ask the user whether they want default or custom generator settings
    print("Would you like to customize the password generator specifications?")
    print("Default Settings: 16 Characters\nUpper case: Allowed\nLower case: Allowed\nNumbers: Allowed\n")

    default_or_custom = input("Enter 'y' to customize, or press enter to go with default settings ")

    if default_or_custom.lower() == "y":
        custom_flag = True
        options = ["y", "n"]

        # Begin taking the custom parameters
        length = input("Password Length: ")
        upper_input = input("Allow upper case? y/n: ")
        lower_input = input("Allow lower case? y/n: ")
        numeric_input = input("Allow numbers? y/n: ")
        punct_input = input("Allow punctuation? y/n: ")

        if upper_input == "y":
            upper_bool = True
        else: 
            upper_bool = False
        
        if lower_input == "y":
            lower_bool = True
        else: 
            lower_bool = False

        if numeric_input == "y":
            numeric_bool = True
        else: 
            numeric_bool = False

        if punct_input == "y":
            punct_bool = True
        else: 
            punct_bool = False


    while True:
        if custom_flag:
            generated_pass = generator.password_generator(length, upper_bool, lower_bool, numeric_bool, punct_bool)  # Call password_gen() and generate an upper+lower password
        else:
            generated_pass = generator.password_generator()
        print(generated_pass)  # Print the password that was just generated

        print("Is this password suitable?")
        reroll_input = input("Enter: 'y' to confirm, 'n' to reroll, or anything else to quit: ")
        if reroll_input.lower() == "y":
            break
        elif reroll_input.lower() == "n":
            continue
        else:
            quit()

    temp_site = input("What site is this password for: ")

    csv_operations.write_password(temp_site, generated_pass)


def take_findpass_input():
    print("Find password by site")
    site_input = input("Enter: Site to search for or 'quit': ")

    if site_input.lower() == "quit":
        quit()
    else:
        print(site_input + " Password: " + csv_operations.read_password(site_input))


def display_menu():
    """ 
        Summary: Display all menu options and execute the option the user chooses
        Variables: 
            options_functions = (Key: The menu number that the user will see. Value: The related function)
            menu_option = Whichever option the from the menu that the user inputted
        Output: 
            1. Generate and save password
            2. Find password
            3. Quit
    """
    options_functions = {"1": take_passwordgen_input, "2": take_findpass_input, "3": quit}

    menu_option = input("1. Generate and save password\n2. Find password\n3. Quit\n")

    if menu_option in options_functions:
        # Clear the console here. No internet at the moment to see how to do this in python
        options_functions[menu_option]()  
    else: 
        input("Sorry, that's not a menu option. Press enter to continue...")  # Error handling
        display_menu()  # Send them back to the beginning
