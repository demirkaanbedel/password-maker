import random

while True:
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    lenght = int(input("How many characters will your password have?"))

    pasword = ""
    for i in range(lenght):
        pasword += random.choice(characters)

    print("I created this pasword for you", pasword)5
