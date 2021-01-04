import random
import string
from words import words

def give_guess_word(words):
    word = random.choice(words)
    if '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = give_guess_word(words)
    word_letter = set(word)
    used_letter = set()
    alphabet = set(string.ascii_uppercase)
    life = 6

    while len(word_letter) > 0 and life > 0:
        print('you have',life, 'lifes to play and you have used these letters:', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('correct word is: ', ' '.join(word_list))

        guess = input('please guess a letter: ').upper()
        if guess in alphabet - used_letter:
            used_letter.add(guess)
            if guess in word_letter:
                word_letter.remove(guess)
            else:
                life -= 1
                print('you guessed wrong letter')
        else:
            print('you\'ve used this letter')

    if life == 0:
        print('sorry, you\'re done')
    else:
        print('cool, you guess the right word')
hangman()