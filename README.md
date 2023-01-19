# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


MileStone 1 was a case of connecting GutHub to the AiCore portal.

Milestone 2 we created a Python List and then used the RANDOM module to pick a random fruit.

Milestone 3: We asked the users for an input.  Namely a guess.

Milestone 4: We needed to check the input was a single character.

Milestone 5: Documentation.

TASK3:

You should use an if statement to check if the letter entered by the user is in the word. Remember that the input should be stored in a variable called "guess" and the randomly picked word should be stored in a variable called "word". You can use the "in" operator to check if a character is in a string. If you think you have done it correctly, remember to use the right indentation for the if statement and just a single space between the "if" keyword and the condition.

TASK4:

I learned how to create a class and within the class, use the magic method 'init' to create some base variables.

in addition, I also learned how to use the random/choice module.

What has become obvious is the difference between "=" and "==".  Where the former tells the code to assign a value to a variable and the latter is used as a comparison tool.

Also the self reference tells python 'this instance' and we used that for every single method defined.

I had missed the 'f-strings' which are new in Python 3.6.  it tells the sytem to allow curly brackets when printing variables in print statements.

We also used pythonic code where possible (small but effective code).  This is a good example, which to be honest, I copied:

  self.word_guessed = list('_'*len(self.word))

These presnet the same results:
        print("Good guess! ", guess, " is in the word.")                    
        print(f"Good guess! {guess} is in the word.")




