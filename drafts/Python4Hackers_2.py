import string
# 1 Create a greeting for your program
print("Welcome to my twitter handle generator!")
# 2 Ask for the user for the name of a Pet.
pet = input("What is the name of your pet? ")
# 3 Ask for the name of the city user was born in
city = input("What is the name of the city you were born in? ")
# Combine pet name with the word cyber as new twitter handle and then add the city they are from.
handle = f"cyber{pet}"
# Output should be "Your new twitter hander and bio @cyberfred from Honolulu"
print(f"Your new twitter handle and bio @{handle} from {city}")