import random

RANDOM = random.randint(1,10)
GUESS = 0
while GUESS != RANDOM:
    GUESS = int(input('Please guess a number between 1 to 10\n'))

    if GUESS > RANDOM:
        print('Too big')
    elif GUESS < RANDOM:
        print('Too small')

print('correct')
