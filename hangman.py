import random
guessed_letters = list()
secret_word_blanks = list()
number_of_char = 0
number_of_wrong_guesses = 0
play_status = True
guess = ''
secret_word = ''
#Generate a secret word
def generate_word():
    global number_of_char
    global secret_word
    txt_file = open("C:\\Users\\simju\\Documents\\Github\\hangman\\sports_words.txt")
    txt_file_words = list(txt_file)
    secret_word = random.choice(txt_file_words).strip()
    number_of_char = len(secret_word)
#Generate blanks for secret word
def generate_secret_word_blanks():
    for count in range(number_of_char):
        secret_word_blanks.append('_')
    print('Guess a sport that has',number_of_char,'letters! You have 6 tries! Good Luck!')
    print(' '.join(secret_word_blanks))
#Prompt player to guess a letter/word and validate input, store letter if valid
def player_guess():
    global guess
    while True:
        guess = input('Guess a letter or the word!').lower()
        if guess.isalpha() == False:
            print('Invalid input. Please guess a letter.')
            continue
        elif guess == secret_word:
            break
        elif len(guess) == number_of_char:
            break
        elif len(guess) != 1:
            print('Invalid input. Please guess a letter.')
            continue
        elif guess in guessed_letters:
            print("You have entered this letter before. Try again.")
            continue
        else:
            guessed_letters.append(guess)
            break
#Check if the secret word contain the letter provided by player or if player guessed the word
def check_correct_letter():
    global number_of_wrong_guesses
    if guess == secret_word:
        for n in range(number_of_char):
            secret_word_blanks[n] = guess[n]
    elif len(guess) ==  number_of_char:
        print('Sorry, you did not guessed the correct word.')
        number_of_wrong_guesses = number_of_wrong_guesses + 1
        tries_left = 6 - number_of_wrong_guesses
        print('You have',tries_left,'more attempt!')
    elif guess in secret_word:
        print('You got it! There is the letter',guess)
        count = -1
        for l in secret_word:
            count += 1
            if guess == l:
                secret_word_blanks[count] = guess
        print(' '.join(secret_word_blanks))
    else:
        number_of_wrong_guesses = number_of_wrong_guesses + 1
        print('Sorry, there is no letter',guess)
        tries_left = 6 - number_of_wrong_guesses
        print('You have',tries_left,'more attempt!')
#Check if player guessed all letters in secret words or used up all attempts
def player_win_or_lose():
    global number_of_wrong_guesses
    global play_status
    if '_' not in secret_word_blanks:
        print('Congratulations! You won! The word is',secret_word)
        guessed_letters.clear()
        secret_word_blanks.clear()
        number_of_wrong_guesses = 0
        play_status = False
    if number_of_wrong_guesses == 6:
        print('Too bad! Better luck next time! The answer is',secret_word)
        guessed_letters.clear()
        secret_word_blanks.clear()
        number_of_wrong_guesses = 0
        play_status = False
#Ask if the player wants to play again
def player_play_again():
    global play_status
    while True:
        player_response = input('Do you want to try again? (Y/N)').upper()
        if player_response == 'Y':
            play_status = True
            break
        elif player_response == 'N':
            print('Thank you for playing!')
            exit()
        else:
            continue

while True:
    print('Welcome to a Game of Hangman!!!')
    generate_word()
    generate_secret_word_blanks()
    while play_status == True:
        player_guess()
        check_correct_letter()
        player_win_or_lose()
    player_play_again()
