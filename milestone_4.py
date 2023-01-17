import random
word_list=['oranges','melon','banana','apples','cherries']
word = random.choice(word_list)

class Hangman:

    def __init__(self,word_list,num_lives):
        self.num_lives = 5
        


    def ask_for_input():
        while True:
            guess = input("Guess a letter: ").lower()
            if guess.isalpha() and len(guess) == 1:
                break
            print("Invalid letter. Please, enter a single alphabetical character.")
        return guess


    def check_guess(guess2):
        if guess2 in word:
            print("Good guess! ", guess2, " is in the word.")
        else:
            print("Sorry, ", guess2, " is NOT in the word.")
    pass

myguess = Hangman.ask_for_input()
Hangman.check_guess(myguess)