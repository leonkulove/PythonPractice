import random

def play():
    RANDOM = random.choice(['r', 'p', 's'])
    GUESS = input('Please choose Rock(r), Paper(p), or Scissors(s)')
    if GUESS == RANDOM:
        return 'you are tie'

    if you_win(GUESS, RANDOM):
        return 'You win'
    else:
        return 'you lose'

#r > s, p > r, s > p
def you_win(X, Y):
    if (X == 'r' and Y == 's') or (X == 'p' and Y == 'r') or (X == 's' and Y == 'p'):
        return True
print(play())