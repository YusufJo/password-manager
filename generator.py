import string
import random

def password_generator(length=16, upper=string.ascii_uppercase, lower=string.ascii_lowercase, digits=string.digits, punctuation=string.punctuation):
    """ Generate Password according to user specifications
        Arguments: Password length(int), A-Z(bool), a-z(bool), 0-9(bool), !@#$(bool)
        :return:
    """
    return ''.join(random.SystemRandom().choice(upper + lower + digits) for i in range(length))
