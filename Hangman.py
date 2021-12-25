#need validation for both word options to filter out any words with special characters

import random
import pwinput
from word_list import wordList

options = 'YN'
game_options = 'AB'
alert = "Option not available."
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

already_guessed = [] #when they guess, validate it's not in this list, if not, write the guess to the list for later validation.
incorrect_guess = [] #when they guess incorrect, append to this list
correct_guess = [] # when they guess correct, append to this list

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
,'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def sep():
    print("_____")
    print()

def ending():
    print()
    print("-"*15)
    print()

def input_valid(message, i=1):
	while True:
		answer = input(message).upper()
		if answer[:i] in options:
			break
		print(alert + ' Try again: ')

	try:
		return int(answer[:i])
	except:
		return answer[:i] == options[:i]

def gameplay_valid(message, i=1):
    while True:
        answer = input(message).upper()
        if answer[:i] in game_options:
            break
        print(alert + ' Try again: ')

    try:
        return int(answer[:i])
    except:
        return answer[:i] == game_options[:i]

def word_choice_valid(): #validation on word entry for multiplayer modern
    while True:
        choice = pwinput.pwinput(prompt='Please select a secret word with 4 to 12 letters: ').upper()
        if int(len(choice)) >= 4 and int(len(choice)) <= 12 and choice.isalpha():
            break
        print('\nPlease select a word that has between 4 and 12 letters and no numbers or special characters.\n')
    return choice

def guess_valid(message): #need to add already guess validation. !!not sure if this belongs here or in gamplay.
    while True:
        letter = input(message).upper()
        if letter in already_guessed:
            print('You already guessed that one.')
        elif letter in alphabet:
            already_guessed.append(letter)
            break
        print(alert + ' Guess again:')
    return letter

def load_word(): #need to add validation somewhere to exclude special characters
    while True:
        word_index = random.choice(wordList)
        if word_index.isalpha():
            break
    return word_index

def clear_list():
    already_guessed.clear()
    incorrect_guess.clear()
    correct_guess.clear()

def select_gamemode(): #setup user input to select single or multiplayer - then branch gameplay function based on input
    gamemode = gameplay_valid("(a) Single Player\n(b) Multi Player\nChoose a gamemode: ")
    return gamemode

def gameplay():
    while True:
        gamemode = select_gamemode()
        if gamemode == True:
            secret_word = load_word().upper()
        else:
            secret_word = word_choice_valid()
        x = list(secret_word) #made this a list
        chances = len(stages)-1
        print('\nYou have ' + str(chances) + ' chances to guess the word!')
        while True:
            print(stages[len(incorrect_guess)])
            print('\nSecret Word: ')
            for k in range(len(x)):
                if str(x[k]) in correct_guess:    #if correct guesses in loaded word, fill in the letters, else print "-"
                    print(str(x[k]), end= ' ')
                else:
                    print('_', end=' ')

            print('\n\nAlready Guessed: ' + str(already_guessed))

            guess = guess_valid('\n\nPick a Letter: ')
            if guess in x:
                sep()
                print("'" + guess + "' is in there!\n")
                correct_guess.append(guess)
            else:
                sep()
                print("No luck :(")
                incorrect_guess.append(guess)

            remaining = chances - len(incorrect_guess)
            print(str(remaining) + " guesses remaining...")
            sep()

            win = True
            for l in range(len(x)): #pull in True if guessed all the letters
                if (x[l]) not in correct_guess:
                    win = False
            if win == True:
                print('YOU WIN!')
                print()
                print('The word is ' + secret_word)
                ending()
                break
            elif len(incorrect_guess) == chances: #check for loss. Incorrect guesses = chances
                print(stages[6])
                print("YOU LOSE!")
                print()
                print('The word is ' + secret_word)
                ending()
                break
            else:
                continue

        replay_choice = input_valid("Play Again? [Y/N]: ")
        if replay_choice == True:
            print("\nThat's the Spirit!\n")
            ending()
            clear_list()
            continue
        print("\nThanks for playing!")
        ending()
        break

print('---Hangman---\n')
gameplay()
