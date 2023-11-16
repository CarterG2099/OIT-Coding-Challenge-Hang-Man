#Carter Gividen
#OIT Student Programming coding challenge
#Hangman

import random
import sys
from hang_man_art import draw_hangman

#Pull list of random words to be used in game
with open('random_words.txt', 'r') as random_words_file:
    random_words_list: list[str] = random_words_file.readlines()

#initialize global variables
MAX_GUESSES = 11
random_word: str = random.choice(random_words_list).strip().lower() #Randomly select a word
correct_guesses: int = 0 #track number of correct guesses
incorrect_guesses: int = 0 #track number of incorrect guesses
incorrect_guess_list: set[str] = set() #track the incorrect gueses without keeping duplicates
guessed_word: list[str] = ["_" for space in range(len(random_word))] #Generate display string that updates with correct guesses

#handle quitting the game
def handle_quit() -> None:
    print("Thanks for playing!")
    sys.exit()

#Handle next step after winning the game
def handle_game_phase(wonGame:bool) -> None:
    if wonGame:
        print(f"\nPhew! You're safe! You've correctly guessed {random_word}!")
        print(f"It took you {correct_guesses + incorrect_guesses} guesses")
    else:
        draw_hangman(incorrect_guesses)
        print(f"Uh no! You've been hanged!")
        
    #Ask if they would like to continue
    while True:
        next_step = input("Would you like to play again? (Y/N)?").strip().lower()
        if next_step == "y":
            print("Bring it on!")
            reset_variables()
            gameplay()
        elif next_step == "n":
            handle_quit()
        else:
            print("Sorry, I didn't understand. Please enter 'Y' or 'N'.")

#Reset the global variables
def reset_variables() -> None:
    global random_word, correct_guesses, incorrect_guesses, incorrect_guess_list, guessed_word
    random_word = random.choice(random_words_list).strip().lower()
    correct_guesses = 0
    incorrect_guesses = 0
    incorrect_guess_list = set()
    guessed_word = ["_" for space in range(len(random_word))]

#Gameplay
def gameplay() -> None:
    global random_word, correct_guesses, incorrect_guesses, incorrect_guess_list, guessed_word
    #Welcome the user to the game and explain rules
    print("Welcome to Hangman!")
    print(f"""Rules are as follows:
        1.You have {MAX_GUESSES} gueses.
        2.Make your guess when prompted.
        3.Repeated guesses will count against you.
        4.Capitalization doesn't matter.
        5.Guess the word in the fewest letters as possible.
        6.You may quit anytime by entering 'Quit'.
        """)  
    
    #Give a clue to the user about the word
    print(f"\nYour word contains {len(random_word)} letters. Good luck!")
    
    #Ask the user to guess a letter
    while True:
        draw_hangman(incorrect_guesses)
        guess = input("\nGuess a letter: ").strip().lower()
        #Case: Quit qameplay
        if guess == "quit":
            handle_quit()
            
        #handle input that is more than one letter
        elif len(guess) != 1:
            print("Please input a single letter")
        
        #If correct - display letter in corresponding location in the word
        elif guess in random_word:
            correct_guesses += 1
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    guessed_word[i] = guess #update the progress of the guest word
                
            #Check if they won the game
            if random_word == ''.join(guessed_word):
                handle_game_phase(True)

            #Congratulate and display correctly guessed letters
            else:    
                print(f"\nNice! The letter '{guess}' is in your mystery word:\n{' '.join(guessed_word)}") 
                
        #If incorrect - Inform it is incorrect
        else:
            incorrect_guess_list.add(guess) #track the letters guessed
            incorrect_guesses += 1
            #Check game over
            if incorrect_guesses >= MAX_GUESSES:
                handle_game_phase(False)
            # display past incorrect guesses
            else:
                print(f"\nSorry, '{guess}' is not in the word :(")
                print(f"You have made {incorrect_guesses} incorrect guesses: {', '.join(incorrect_guess_list)}")
                print(f"{' '.join(guessed_word)}") #display current progress of the word
            
        #Display running total guesses
        print(f"\nTotal Guesses: {incorrect_guesses + correct_guesses}") #total guesses
        print(f"Correct: {correct_guesses}") #Number of correct guesses
        print(f"Incorrect: {incorrect_guesses}") #Number of incorrect gueses
            
#begine game
gameplay()

#close file
random_words_file.close()
