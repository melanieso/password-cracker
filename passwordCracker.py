# This project requires us to import some libraries

# urllib is a package that collects several modules for working with URLs
# urlopen fetches URLs
# hashlib implements a common interface to many different secure hash and message digest algorithms

from urllib.request import urlopen, hashlib

# STEP 1: Get the SHA-1 Hash from the user

# For this program, the user will need to input a SHA-1 hash rather than a plain text password
# Plain text can be hashed using websites such as http://www.sha1-online.com/
sha1hash = input("Input the hash to crack :) ")

# STEP 2: Open a file of common passwords

# str() is used so that our program knows it is reading text from a file. Similarly, we provide the argument 'utf-8'
# to indicate that we are using UTF-8 encoding.
LIST_OF_COMMON_PASSWORDS = str(
    urlopen(
        'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),
    'utf-8'
)

# STEP 3: Guess from the list of passwords
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    # We use hashlib to turn each password in the file into a SHA-1 hash. In order to
    # use this function, we need to cast each password into a bytes object first.
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ", str(guess),
              " does not match :( attempting next hash")

print("The hash inputed does not belong to one of the 10,000 most commonly used passwords")
