import random
import string

print("Welcome to Password Generator")
print("------------------------------")

length = int(input("Enter password length: "))

print("Include numbers? (yes/no): ", end="")
use_numbers = input()

print("Include symbols? (yes/no): ", end="")
use_symbols = input()

chars = string.ascii_letters

if use_numbers == "yes":
    chars = chars + string.digits

if use_symbols == "yes":
    chars = chars + "!@#$%&*"

password = ""

for i in range(length):
    password = password + random.choice(chars)

print("")
print("Your password is:", password)
