import random
word_list=['oranges','melon','banana','apples','cherries']
word = random.choice(word_list)

while True:
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        break
    print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print("Good guess! ", guess, " is in the word.")
else:
    print("Sorry, ", guess, " is NOT in the word.")