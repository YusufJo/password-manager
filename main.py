import generator

"""
    TODO: Make a menu system
    TODO: Allow for custom passwords
    TODO: Make a UI
    TODO: Encrypt Password Bank. To ensure proper security and comply with common sense, the password bank NEEDS to be encrypted.
    TODO: Generate passwords using properly secure random methods. Currently using system random which is not ideal according to people in the cryptography community.
    TODO: Fix writing passwords. Currently passwords get overwritten and never get added to a second line.
"""

def main():
    print(generator.password_generator())

if __name__ == '__main__':
    main()
