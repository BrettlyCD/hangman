import random

options = 'YN'
game_options = 'AB'
alert = "Option not available."
dictionary = ['notice','barbarous','legal','useless','devilish','unused','mate','trust','six','building','stick','ocean','brash','drown','bone','launch','puncture','painful','few','fog','drum','powder','wander','deranged','combative','zoo','tire','possible','annoyed','explode','determined','tightfisted','serious','judicious','unusual','shiver','writing','animal','jellyfish','tired','tall','unequaled','curl','pastoral','parched','imminent','multiply','name','sin','dust','island','tank','scent','bucket','produce','repair','cheese','furniture','bee','swing','event','command','border','common','complex','escape','tangy','undesirable','melt','wren','suck','last','jumbled','license','young','toy','observe','crowd','sack','offbeat','tow','wail','ants','royal','wet','squeak','thin','outgoing','check','rejoice','salty','gainful','pumped','pest','unarmed','prevent','number','squeeze','forgetful','oval','describe','wistful','stranger','talk','insect','peel','busy','creator','store','colour','annoying','soft','chubby','arithmetic','overrated','rake','quiver','healthy','surround','average','embarrassed','clean','spurious','rhythm','swift','immense','crib','brawny','dislike','modern','zephyr','dramatic','scattered','contain','hang','continue','pet','murder','awesome','polish','maid','far-flung','flower','fool','dance','chance','obtain','expect','pan','gleaming','loaf','gruesome','blow','shake','wink','bathe','exuberant','knife','zip','married','strange','horn','expand','hands','fish','payment','weight','happen','mend','belief','wise','flight','scrawny','festive','art','utopian','chunky','strap','plucky','sleep','truthful','fire','silk','lumpy','spiffy','agonizing','pigs','picture','itchy','plastic','violent','sassy','van','ceaseless','lazy','useful','pie','aunt','company','corn','late','chess','ugly','fuzzy','public','tendency','serve','ticket','blush','auspicious','hushed','squalid','humorous','wreck','scale','necessary','steady','unkempt','tie','sock','cynical','wonder','likeable','economic','rebel','dinosaurs','committee','lumber','accurate','fine','wait','shape','deep','chew','gaudy','bushes','bang','fallacious','spiders','vacuous','zebra','mitten','confess','kindhearted','voiceless','brick','vigorous','stamp','fantastic']
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

def word_choice_valid(message): #validation on word entry for multiplayer modern
    while True:
        choice = input(message).upper()
        if int(len(choice)) >= 4 and int(len(choice)) <= 12:
            break
        print('Please select a word that has between 4 and 12 letters: ')
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

def load_word(): #can plug option for different dictionaries - easy, medium, hard - based on user input at start of game
    word_index = random.choice(dictionary)
    return word_index

#def reveal():
 #   print('The word is {}'.format(word_index)) #need to learn how to put future inputs into function

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
            secret_word = word_choice_valid("Please select a secret word with 4 to 12 letters: ")
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

print('---Hangman---')
gameplay()
