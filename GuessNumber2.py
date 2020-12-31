import random

RANDOM = random.randint(1, 10)
GUESS = 0
while GUESS != RANDOM:
    GUESS = int(input('Please guess a number between 1 to 10\n'))

    if GUESS > RANDOM:
        print('Too big')
    elif GUESS < RANDOM:
        print('Too small')

print('correct')

# Another guess number by computer
def computer_guess(x):
    min = 1
    max = x
    feedback = ''
    while feedback != 'c':
        if min != max:
            computer_guess = random.randint(min, max)
        else:
            computer_guess = min

        feedback = input(f'is computer guess: {computer_guess} too high(h) or too low(l), or correct(c)?')
        if feedback == 'h':
            max = computer_guess - 1
        elif feedback == 'l':
            min = computer_guess + 1
    print('correct')

computer_guess(10)