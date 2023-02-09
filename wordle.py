# create a wordle clone
# 
# main program

import sys
import os
import argparse
import random

# this game will be command-line driven
# a random word is selected from a list
# the word will be five characters long
# the user will be prompted to guess the word

# the user will enter five letters

# the program will check the letters against the word
# if the letter is in the word, it will be displayed
# if the letter is not in the word, it will be displayed with an x
# if the user cannot guess the word in six tries, they lose

# the user will be prompted to play again
# if the user enters y, the game will restart
# if the user enters n, the game will end


# this function will select a random word from the word list
def select_word():
    # open the word list
    with open('wordlist.txt', 'r') as f:
        # read the file into a list
        word_list = f.readlines()
        # select a random word from the list
        word = random.choice(word_list)
        # remove the newline character
        word = word.rstrip()
        # return the word
        return word
    
# the main function will run the game
def main():
    # call word selection function to get a word
    word = select_word()
    # create a variable to hold the number of guesses
    guesses = 0
    # while guesses is less than or equal to six
    while guesses <= 6:
        # prompt the user to enter the word using print()
        print('Guess the word: ', end='')
        # read the user's input using input()
        guess = input()
        # compare the user's input to the word
        if guess == word:
            # if the user's input matches the word, display a congratulations message
            print('Congratulations! You guessed the word!')
            # prompt the user to play again
            print('Would you like to play again? (y/n): ', end='')
            # read the user's input
            play_again = input()
            # if the user enters y, restart the game
            if play_again == 'y':
                # call the main function
                main()
            # if the user enters n, end the game
            elif play_again == 'n':
                # exit the program
                sys.exit()
        # else if the word is not guessed, replace the 
        # letter with an x
        else:
            # create a variable to hold the new word
            new_word = ''
            # loop through the word
            for letter in word:
                # if the letter is in the word, add it to the new word
                if letter in guess:
                    new_word += letter
                # else if the letter is not in the word, add an x
                else:
                    new_word += 'x'
            # print the new word
            print(new_word)
            # print the number of guesses
            print('Guesses: ' + str(guesses))
            
            # increment the number of guesses
            guesses += 1

# if main is called, run the game
if __name__ == '__main__':
    main()
