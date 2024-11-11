import random

def parola():

    lenght = 10

    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(lenght):
        
        random_character = random.choice(characters)
        
        password += random_character

    return password