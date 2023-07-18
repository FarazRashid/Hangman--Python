from words import words
import random

def get_word():
    max_number=words.__len__()
    return(words[random.randint(0,max_number)])
    
    
def play_Hangman():
    word_to_guess=get_word()
    lives=word_to_guess.__len__()

    guessed_letters=[]

    while lives>0:
        letter=input("Please enter a letter : ")

# validation
        for letters in guessed_letters:
            while letters==letter:
                print("You have already entered this letter into the program please try again")
                letter=input("Please enter a letter : ")

        if letter not in word_to_guess:
            lives-=1

        guessed_letters.append(letter)

        print("You have "+ str(lives) + " left and you have guessed these letters: " + str(guessed_letters))
        print("")

        print("current word: ")

        for letter in word_to_guess:
                    print("_ ")
            



play_Hangman()
