import random

while True:
    number = random.randint(0, 99)
    guessNum = int(input("Guess Number (0-99): "))
    if(guessNum == number):
        print("You guessed the number!")
    elif(guessNum > number):
        print("Too high!")
    else:
        print("Too low!")