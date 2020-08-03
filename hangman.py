import random
#Open file, choose random word, create start state
fhand = open("C:\\Users\\simju\\Documents\\Github\\hangman\\sports_words.txt")
words = list(fhand)
list_of_letters = list()
current_guess_status = list()
response = 'Y'
def start_game():
    number_of_char = len(word)
    for each_letter in word:
        current_guess_status.append('_')
    print('Guess a sport that has',number_of_char,'letters! You have 6 tries! Good Luck!')
    print(current_guess_status)
#Create a list and function to check valid inputs
def check_valid(wrong,count):
    while wrong < 6:
        guess = input('Guess a letter')
        if guess.isalpha() == False:
            print('Invalid input. Please guess a letter.')
            continue
        else:
            check_letter = guess.lower()
        if check_letter in list_of_letters:
            print("You have entered this letter before. Try again.")
            continue
        if check_letter not in word:
            wrong = wrong + 1
            tries = 6 - wrong
            print('Sorry, there is no letter',check_letter)
            print('You have',tries,'more attempt!')
        else:
            print('You got it! There is the',check_letter)
        if len(list_of_letters) == 0:
            list_of_letters.append(check_letter)
        else:
            list_of_letters.append(check_letter)
        for letter in word:
            count = count + 1
            if letter == check_letter:
                current_guess_status[count] = letter
        if '_' not in current_guess_status:
            print('Congratulations! You won! The word is',word)
            list_of_letters.clear()
            current_guess_status.clear()
            break
        else:
            print(current_guess_status)
        count = -1
        if wrong == 6:
            print('Too bad! Better luck next time! The answer is',word)
            list_of_letters.clear()
            current_guess_status.clear()
print('Welcome to a Game of Hangman!!!')
while response == 'Y':
    word = random.choice(words).strip()
    start_game()
    check_valid(0,-1)
    response = input('Do you want to try again? (Y/N)')
    if response == 'Y':
        continue
    elif response == 'N':
        break
