from words import words
import random

def get_word():
    max_number=words.__len__()
    return(words[random.randint(0,max_number)])
    
    



def play_Hangman():
    word_to_guess=get_word()

    guessed_letters=[]

    while True:
        letter=input("Please enter a letter : ")
        guessed_letters.append(letter)

        print("You have guessed these letters so far: ")
        for letters in guessed_letters:
            print(letter)

play_Hangman()
