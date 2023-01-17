import random

class Hangman:
    word_list=['oranges','melon','banana','apples','cherries']

    def __init__(self):
        self.num_lives = 5
        self.word = random.choice(self.word_list)
        self.wordguessed = []
        self.num_letters = 0
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if guess.isalpha() and len(guess) == 1:
                break
            print("Invalid letter. Please, enter a single alphabetical character.")

        if guess in self.word:
            print("Good guess! ", guess, " is in the word.")
        else:
            print("Sorry, ", guess, " is NOT in the word.")
    pass

myguess = Hangman().ask_for_input()
