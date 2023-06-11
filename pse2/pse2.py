''' question
Imagine programming the logic for a word game.

In this game, every player submits one word. Each word gets a score based on the letters in the word and its point value.

Create a function named score that is responsible for scoring a given word.

This function should take in a string named word as a parameter. This function should return the word's total number of points.

Refer to this table for the point values of each letter.
'''

''' feedback
Love it! Short and sweet, and good idea refactoring to let the dictionary's advantages shine.

One thing maybe to consider is a check to make sure the letter is in the dictionary to avoid a potential raised error.
'''

def score(word):
    # refactored from project, to lower time complexity
    LETTER_SCORES = {
        "A" : 1, 
        "E" : 1, 
        "I" : 1, 
        "O" : 1, 
        "U" : 1, 
        "L" : 1, 
        "N" : 1, 
        "R" : 1, 
        "S" : 1, 
        "T" : 1,
        "D" : 2, 
        "G" : 2,
        "B" : 3, 
        "C" : 3, 
        "M" : 3, 
        "P" : 3,
        "F" : 4, 
        "H" : 4, 
        "V" : 4, 
        "W" : 4, 
        "Y" : 4,
        "K" : 5,
        "J" : 8, 
        "X" : 8, 
        "Q" : 10, 
        "Z" : 10,
    }
    score = 0
    
    for letter in word.upper():
        if letter.isalpha():
            score += LETTER_SCORES[letter]
    
    return score