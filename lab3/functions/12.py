


# 12
# Define a function histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
print("!!!TASK 12!!!")
def histogram(values):
    curr = '*'
    for val in values:
        if val != 0:
            curr = curr * val
        else:
            curr = ''
        print(curr)
        curr = '*'


# histogram([1, 0, 2, 0, 3])

# Write a program able to play the "Guess the number" - game,
# where the number to be guessed is randomly chosen between 1 and 20. 
# This is how it should work when run in a terminal:
"""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""


import random
name = input("Hello! What is your name?")
print("Well, KBTU, I am thinking of a number between 1 and 20.")

guessed_num = random.randint(1, 20)
guess = 0
num_guesses = 0
while guess != guessed_num:
    print("Take a guess")
    guess = int(input())
    num_guesses += 1
    if guess < guessed_num:
        print('Your guess is too low.')
    elif guess > guessed_num:
        print('Your guess is too high')
    else:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break









