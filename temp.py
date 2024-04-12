import random
import string

def generate_random_password():
    length = random.randint(7,10)
    password = ""
    for _ in range(length):
        password += ''.join(chr(random.randint(33,126)))
    return password

random_password = generate_random_password()
print(random_password)