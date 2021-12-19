import random

print("Welcome to number guessing Game!")
number = random.randint(1,9)

chances = 1

print("Guess a number between 1-9!")

while chances<=5:
    guess = int(input("enter your number: "))
    if(guess == number):
        print("congratulations you won !")
        break
    elif(guess<number):
        print("your guess was too low guess a number higher than ",guess)
    else:
        print("your guess was too high guess a number lower than ",guess)

    chances = chances+1

if(chances > 5):
    print("oh ho you lose!! the number was ",number)