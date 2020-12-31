import random

print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
Think=random.randint(1, 20)

i = 0
while True:
 Guess = int(input())
 if Guess > Think:
    print('your guess is too high')
    print('Take a guess.')
    i = i + 1
    continue
 elif Guess < Think:
      print('your guess is too low')
      print('Take a guess.')
      i = i + 1
      continue
 elif Guess == Think:
      print('Good job')
      i = i + 1
      break
print('guess ' + str(i) + ' times')
print('my thinking is ' + str(Think))