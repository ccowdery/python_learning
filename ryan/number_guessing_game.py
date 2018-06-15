import random

to_be_guessed = random.randint(1,100)

user_guess = 0

print("Guess a number from 1 to 100.")

while user_guess != to_be_guessed:
    
    user_guess = int(input('Guess:'))
    if user_guess > to_be_guessed:
        print("Too High!")
    if user_guess < to_be_guessed:
        print("Too Low!")
    if user_guess == to_be_guessed:
        print("You Got It!")
