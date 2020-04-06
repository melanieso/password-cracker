# This project requires us to import some libraries

# urllib is a package that collects several modules for working with URLs
# urlopen fetches URLs
# hashlib implements a common interface to many different secure hash and message digest algorithms

from urllib.request import urlopen, hashlib

# STEP 1: Get the SHA-1 Hash from the user

sha1hash = input("Input the hash to crack :) ")


# STEP 2: Open a file of common passwords
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
        print("Password guess ", str(guess), " does not match, trying next...")

print("The password is not part of the 10000 most common")
