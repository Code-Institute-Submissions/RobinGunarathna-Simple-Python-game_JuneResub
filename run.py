import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_complete = "_" * len(word)
    guess = False
    guess_letters = []
    guess_words = []
    attempts = 6
    print("Play hangman!")
    print(display_hangman(attempts))
    print(word_complete)
    print("\n")
    while not guess and attempts > 0:
        guessed = input("Guess a letter or a word: ").upper()
        if len(guessed) == 1 and guessed.isalpha():
            if guessed in guess_letters:
                print("you allready guessed", guessed)
            elif guessed not in word:
                print(guessed, "is not in the word")
                attempts -= 1
                guess_letters.append(guessed)
            else:
                print("good!", guessed, "is in the word!")
                guess_letters.append(guessed)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guessed]
                for index in indices:
                    word_as_list[index] = guessed
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guess = True
        elif len(guessed) == len(word) and guessed.isalpha():
            if guessed in guess_words:
                print("you allready guessed the word", guessed)
            elif guessed != word:
                print(guessed, "is not the word")
                attempts -= 1
                guess_words.append(guessed)
            else:
                guess = True
                word_complete = word
        
        else:
            print("not a valid quess")
        print(display_hangman(attempts))
        print(word_complete)
        print("\n")
    if guess:
        print("you guessed the word you win!")
    else:
        print("You ran out of attempts. The word was " + word + "Try again?")

def display_hangman(attempts):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()