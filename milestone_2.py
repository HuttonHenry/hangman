import random
    
word_list=['oranges','melon','banana','apples','cherries']
word = random.choice(word_list)
print(word)

guess = input("enter a single letter")

if len(guess) == 1 and type(guess) == str:
    print("Good guess!")
else:
    print("Oops!")


