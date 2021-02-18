import string
import secrets


def password_generator(length=16, allow_upper=True, allow_lower=True, allow_digits=True, allow_punctuation=True):
    """ Generate Password according to user specifications
        Arguments: Password length(int), A-Z(bool), a-z(bool), 0-9(bool), !@#$(bool)
        :return:
    """
    bool_list = [allow_upper, allow_lower, allow_digits, allow_punctuation]  # List of the args the user gave, or defaulted. Probably not the best way to do this, but I don't have internet.
    elements = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]  # Upper, lower, digits, punctuation. Will be added to pass elements
    pass_elements = []  # Where we store the types of characters that the user wants to comprise the password

    for i in range(len(bool_list)):  # For every bool arg
        if bool_list[i] == True:  # If the current bool is set to True...
            pass_elements += elements[i]  # ...Add it to the valid password elements list

    return ''.join(secrets.SystemRandom().choice(pass_elements) for i in range(int(length)))  # Return a password made using the parameters the user specified
 