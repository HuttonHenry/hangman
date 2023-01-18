# generate random word.
import random
word_list=['oranges','melon','banana','apples','cherries']
word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:  
            break
        else:          
            print("Invalid letter. Please, enter a single alphabetical character.")
        return guess

def check_guess(guess):
    print(word)
    if guess in word:
        print("Good guess! ", guess, " is in the word.")
    else:
        print("Sorry, ", guess, " is NOT in the word.")

myguess = ask_for_input()
check_guess(myguess)