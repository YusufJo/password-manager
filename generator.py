import string
import secrets

# def password_generator(length=8, upper=string.ascii_uppercase, lower=string.ascii_lowercase, digits=string.digits, punctuation=string.punctuation):
# return ''.join(random.SystemRandom().choice((string.ascii_uppercase if allow_upper else '') + (string.ascii_lowercase if allow_lower else '') + (string.digits if allow_numbers else '') + (string.punctuation if allow_symbols else '')) for i in range(length))
#elements = upper + lower + digits + punctuation

def password_generator(length=16, allow_upper=True, allow_lower=True, allow_digits=True, allow_punctuation=True):
    """ Generate Password according to user specifications
        Arguments: Password length(int), A-Z(bool), a-z(bool), 0-9(bool), !@#$(bool)
        :return:
    """
    bool_list = [allow_upper, allow_lower, allow_digits, allow_punctuation]
    elements = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
    pass_elements = []

    for i in range(len(bool_list)):
        if bool_list[i] == True: 
            pass_elements += elements[i]
        else: 
            pass


    return ''.join(secrets.SystemRandom().choice(pass_elements) for i in range(int(length)))
    # return ''.join(random.SystemRandom().choice(upper + lower + digits + punctuation) for i in range(length))


