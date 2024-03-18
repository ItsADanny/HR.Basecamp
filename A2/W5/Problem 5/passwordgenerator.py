# Import the required function
import random
import string

def generate_random_password():
    # Generate a random length for the password
    length = random.randint(7, 10)
    # Retrieve all the ascii characters that are allowed to be used for this problem
    ascii = string.ascii_letters + string.digits + string.punctuation
    # Define a string in which the password will be stored
    password = ""
    # Do a for-loop with a range function based on the random length for the password we generated earlier
    for i in range(length):
        # Add the randomly selected character to the password string
        password += ascii[random.randint(0, (len(ascii) - 1))]

    print(password)

generate_random_password()