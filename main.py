from words import words
import random

def get_word():
    max_number=words.__len__()
    return(words[random.randint(0,max_number)])
    
    
def play_Hangman():

    print("Welcome to hangman!")
    userinput=input("Please press 's' button to start the game: ").lower()
    while userinput=='s':
        word_to_guess="apple"
        lives=word_to_guess.__len__()
        total_letters=lives
        letters_guessed=0

        display_flags=[False for letters in range(lives)]

        guessed_letters=[]

        while lives>0 and guessed_letters!=total_letters:
            letter=input("Please enter a letter : ")

    # validation
            for letters in guessed_letters:
                while letters==letter:
                    print("You have already entered this letter into the program please try again")
                    letter=input("Please enter a letter : ")

            if letter not in word_to_guess:
                lives-=1

            guessed_letters.append(letter)

            x=0

            for i in word_to_guess:
                if letter==i:
                    display_flags[x]=True
                    letters_guessed+=1
                x+=1

            print("You have "+ str(lives) + " left and you have guessed these letters: " + str(guessed_letters))
            print("")

            print("current word: ")

            x=0

            for i in display_flags:
                if i==False:
                    print("_",end=" ")
                elif i==True:
                    print(word_to_guess[x],end=" ")
                x+=1
            
            print("")

            if(letters_guessed==total_letters):
                print("You have won the game! Congratulations")
                break
            
        if(letters_guessed!=total_letters and lives<=0):
                
                print("You have lost the game! You have ran out of lives")
                break
        
        print("")
        userinput=input("Please press 's' if you'd like to continue otherwise you will exit: ").lower()

    print("Thank you for playing!")



play_Hangman()
