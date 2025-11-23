#HANGMAN GAME
def hangman():
# def is used to define the fucntion 
    word_list=["hangman","certificate","zigzag","admission","wizard","pirate","jenga","castle","stack","cursor","mystery","function","acceleration","bridge","support"]
    import random
    word=random.choice(word_list)
    #enable to chose random word from the list
    
    print("            HANGMAN GAME                ")
    print("                  _")
    print("                 |_|")
    print("                 -|-")
    print("                 _|_")
    print("\n          LET'S PLAY THE GAME            \n")
    print("------------GUESS THE WORD--------------")
    
    guess_word=[]
    guess=[]
    lives=9
    #it takes 9 steps to make the hangman
    
    correct_guesses=[]
    #to keep a track of all the correct guesses made by the user
    
    while True:
        progress=''
        print("\nTHE WORD IS:")
        
        for i in word:
        # to store blank spaces and correct guesses in a string
            if i in correct_guesses:
                progress+=" "+i+' '
            else:
                progress+=" ___ "
        print(progress)

        if " ___ " not in progress:
        # the winning condition
            print("YOU WON!!!!\nTHE WORD WAS,",word)
            break
        
        if lives>0:
            guessed_letter=input("ENTER YOUR GUESSED ALPHABET:")
            guessed_letter=guessed_letter.lower()
            #converts the guessed alphabet into lowercase
            correct_guesses.append(guessed_letter)
            
            if guessed_letter in word:
            #for the correct guess by the user for the word
                print("CORRECT GUESS!!")
                if guessed_letter in guess:
                    print("ALREADY GUESSED THIS LETTER")
                # to store all the correct guesses in the list
                
            else:
                if guessed_letter in guess:
                    print("ALREADY GUESSED THIS LETTER")
                else:
                    lives-=1
                    print("GUESSED WRONG LETTER!!:(")
                    print("REMAINING ATTEMPTS: ",lives)
                # helps user to keep track of their remaining attempts
                
            guess.append(guessed_letter)
            if len(guessed_letter)!=1:
                print("ENTER SINGLE ALPHABET ONLY!")
            # in case more than one letter is inputted
            
        else:
            print("YOU LOST!!!:(\nTHE WORD WAS:",word)
            # if all lives are used
            break

# the main-menu program for endless game
def main_menu():
    while True:
    # while loop will help to make the game endless until user input n in ch
        ch=input("DO YOU WANT TO PLAY THE GAME TYPE Y FOR YES AND N FOR NO:")
        # choice for user if they want to play again
        if ch=="Y":
            hangman() # calling hangman function
        else:
            print("\nTHANKS FOR PLAYING!!\nHAVE A NICE DAY!!\n:)")
            break

main_menu() # calling main menu function
