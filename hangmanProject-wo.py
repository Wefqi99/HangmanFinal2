#Wefqi's Sprint 8 Hangman Project
#Examples used from video by Kylie Ying
#link: https://www.youtube.com/watch?v=cJJTnI22IF8






import random 
from words import words
import string
from pictures import pictures



def getAWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()



def hangmanGame():
    word = getAWord(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()


    lives = 9

    while len(wordLetters) > 0 and lives > 0:
        print('You currently have', lives, 'lives left and you have used the following letters: ', ' '.join(usedLetters))

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ',' '.join(wordList))
        


        userLetter = input('Please Guess a Letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)



            else:
                lives = lives - 1  #Takes away a life if the letter is wrong
                print('This is not a letter in the word')


        elif userLetter in usedLetters:
            print('You have already used that letter. Please try again.')

        else:
            print('You have typed an invalid character')



    if lives == 0:
        print('Sorry, you have died. The word was:', word)
    else:
        print('You have guessed the correct word:', word, '!')
    




hangmanGame()
    

    




    









