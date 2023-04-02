from shlex import join
import string
from random import *

upper_= string.ascii_uppercase
lower_=string.ascii_lowercase
digits_=string.digits
letters_=string.ascii_letters


password= " ".join(choice(upper_+lower_+digits_+letters_)) * for i in range(randint(4,8)):

print(password)





