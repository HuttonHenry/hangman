import random

class Hangman:
    word_list=['oranges','melon','banana','apples','cherries']

    def __init__(self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.unique_letters = set(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
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
