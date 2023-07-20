from words import words
import random

def get_word():
    return random.choice(words)
    
    
def play_Hangman():
    
    print("Welcome to hangman!")
    userinput=input("Please press 's' button to start the game: ").lower()
    
    while userinput=='s':
        word_to_guess="snake"
        lives=len(word_to_guess)
        total_letters=lives
        letters_guessed=0
        currentword=""

        

        guessed_letters=set()

        while lives>0 and currentword!=word_to_guess:
            letter=input("Please enter a letter : ")

    # validation
            for letters in guessed_letters:
                while letters==letter:
                    print("You have already entered this letter into the program please try again")
                    letter=input("Please enter a letter : ")

            if letter not in word_to_guess:
                lives-=1

            guessed_letters.add(letter)



            print("You have "+ str(lives) + " left and you have guessed these letters: " + " ".join(sorted(guessed_letters)))
            print("")

    

            currentword="".join(letter if letter in guessed_letters else '-' for letter in word_to_guess)
            print("current word: ", currentword)

            
            print("")

        if(currentword!=word_to_guess):
            print("You have won the game! Congratulations")
            break
            
        if(lives<=0):
                
                print("You have lost the game! You have ran out of lives")
                print("The word was : " + word_to_guess)
                break
        
        print("")
        userinput=input("Please press 's' if you'd like to continue otherwise you will exit: ").lower()

    print("Thank you for playing!")



play_Hangman()
