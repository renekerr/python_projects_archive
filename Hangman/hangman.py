
#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Step 2

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#Step 4
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#TODO-2: - If guess is not a letter in the chosen_word,
#Then reduce 'lives' by 1. 
#If lives goes down to 0 then the game should stop and it should print "You lose."

#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

#Step 5
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]

#TODO-2: - Import the stages from hangman_art.py and make this error go away.

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

#TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.


import random
from mod_hangman_art import *
from mod_hangman_words import *

import os
def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/OS X
        os.system('clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for item in range(word_length):
    display.append('_') # or simply use display += '_'

# Rules
print('IMPORTANT')
print('\t-Guess a letter at a time.')
print('\t-Numbers or special characters are not allowed.')
print('\t-You can try up to six times.\n')

while not end_of_game:
    # User input
    guess = input('Guess a letter: ').lower()
    clear_screen()

    # Ensure the user's input is a single letter
    if len(guess) == 1 and guess.isalpha():
        if guess in display: 
            print(f"You've already guessed the letter {guess}")

        # Loop through each position in the chosen_word
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f'Current position {position}\nCurrent letter {letter}\nGuessed letter {guess}')
            if guess == letter:
                display[position] = letter

        print(f"{' '.join(display)}")  
    
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You have {lives} lives left.")
            
            if lives == 0:
                end_of_game = True
                print(f"Sorry, you lose!. Chosen word to guess was '{chosen_word}'")

        if not '_' in display:
            end_of_game = True
            print('Congrats, you win.')

        print(stages[lives])
    else:
        print('Enter a single letter, please. Try again')
        # Quit game or keep trying
        #end_of_game = True 


