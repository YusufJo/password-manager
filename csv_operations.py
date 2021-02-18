
"""
    TODO: Make the filepath more variable
    TODO: Check to see if the password bank exists, create it if not
    TODO: Encrypt the password bank
"""

filepath = "password_bank.csv"  # The designated password bank.


def write_password(site, password):
    """ 
        Summary: Store the generated password in the designated filebank
        Output: In the designated encrypted password bank file, "Website,OwiDh8awy72"
    """
    global filepath

    file_object = open(filepath, "a")  # Open the password bank (writeonly), name/path of which is stored in the filepath global var
    file_object.write(site + "," + password + "\n")  # Write to the file in the proper format, end with a newline char

    file_object.close()  # Close the password bank


def read_password(site):
    global filepath
    
    file_object = open(filepath, "r")  # Open the password bank (readonly), name/path of which is stored in the filepath global var
    file_lines = file_object.readlines()  # Read and store all the lines in the file in this variable
    
    for i in file_lines:
        if site in i:  # If the site name is in the current line
            password_line = i.split(",")  # Split the line at the delimeter ','
            file_object.close()  # Close the password bank
            return password_line[1]  # Return index 1 of the line, which should be the password
    return "Site / Password not found!"  # If it goes through every line and can't find the site, return nothing found