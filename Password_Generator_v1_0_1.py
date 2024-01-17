# Password_Generator_v1_0_1

import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#£$%&/{}()[]=?+\\^'*-_.:,;<>"
extra = '"´¤`¨~|½§öäåàáâãéêõóôúíçÖÄÅÀÁÂÃÉÊÕÓÔÚÍÇ'

choosen_characters = ""
password = ""

while True:
    choice1 = str(input('Do you want upper-case letters in your password? (Please answer with "yes" or "no": ')).lower()
    if choice1 == "yes":
        upper = True
        choosen_characters += uppercase
        break
    elif choice1 == "no":
        upper = False
        break
    else:
        print("Invalid input!""\n")

while True:
    choice2 = str(input('Do you want lower-case letters in your password? (Please answer with "yes" or "no": ')).lower()
    if choice2 == "yes":
        lower = True
        choosen_characters += lowercase
        break
    elif choice2 == "no":
        lower = False
        break
    else:
        print("Invalid input!""\n")

while True:
    choice3 = str(input('Do you want numbers in your password? (Please answer with "yes" or "no": ')).lower()
    if choice3 == "yes":
        num = True
        choosen_characters += numbers
        break
    elif choice3 == "no":
        num = False
        break
    else:
        print("Invalid input!""\n")

while True:
    choice4 = str(input('Do you want symbols in your password? (Please answer with "yes" or "no": ')).lower()
    if choice4 == "yes":
        sym = True
        choosen_characters += symbols
        break
    elif choice4 == "no":
        sym = False
        break
    else:
        print("Invalid input!""\n")

while True:
    choice5 = str(input('Do you want rare symbols in your password? (Please answer with "yes" or "no": ')).lower()
    if choice5 == "yes":
        ext = True
        choosen_characters += extra
        break
    elif choice5 == "no":
        ext = False
        break
    else:
        print("Invalid input!""\n")

while True:
    try:
        length = int(input("How many characters in the password? (min.15, max.50) - Please insert integer number only: ""\n"))
        if 15 <= length <= 50:
            break
    except ValueError:
        print("Invalid input!""\n")

while True:
    try:
        amount = int(input("How many passwords do you want? (min. 1, max. 50) - Please insert integer number only: ""\n"))
        if 1 <= length <= 50:
            break
    except ValueError:
        print("Invalid input!""\n")

# random password generator
for i in range(amount):
    while len(password) < length:
        password += "".join(random.choice(choosen_characters))
    print(f"Password {i+1}: {password}")
    password = ""

# calculating your possible password character combinations
possibilities = "{:.2e}".format(len(choosen_characters)**length) # scientific notation
print("\n"f"You have {possibilities} different password combinations")
print(f"({len(choosen_characters)**length})") # normal notation
print("\n""chararacters in use",len(choosen_characters),"\n")