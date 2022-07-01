import random
import warnings
from constants import stage_dictionary as stages, word_list
from errors import *
 
def get_word():
    word = random.choice(word_list)
    return word.upper()
 
def is_word(_input):
    if len(_input) > 1:
        return True
    else:
        return False
 
def play(word):
    word_as_list = list(word)
 
    failed_attempts = []
 
    guessed = False
    guessed_letters = []
 
    attempts = 0
 
    print("Play hangman!")
    print(display_hangman(attempts))
    print(' '.join(char_ if char_ in guessed_letters else "_" for char_ in word_as_list))
    print("\n")
 
    while not guessed and attempts < 6:
        try:
            current_attempt = input("Guess a letter or a word: \n").upper()
            if current_attempt.isdigit():
                raise InputIsNumberError("Numbers aren't allowed, try again.")
 
            if not is_word(current_attempt):
 
                if current_attempt in guessed_letters or current_attempt in failed_attempts:
                    attempts += 1
                    raise LetterAlreadyInsertedError(f"You already inputted {current_attempt}")
 
                elif current_attempt not in word:
                    attempts += 1
                    failed_attempts.append(current_attempt)
                    raise WrongInputError(f"{current_attempt}, is not in the word!")
 
                else:
                    print(f"Good!! {current_attempt} is in the word!")
                    guessed_letters.append(current_attempt)
                    current_word = [char_ if char_ in guessed_letters else "_" for char_ in word_as_list]
 
                    if "_" not in current_word:
                        guessed = True
            else:
                if current_attempt == word:
                    guessed = True
                elif current_attempt in failed_attempts:
                    attempts += 1
                    raise WordAlreadyTriedError(f"You already tried the word {current_attempt}.")
                else:
                    attempts += 1
                    failed_attempts.append(current_attempt)
                    raise WrongInputError(f"{current_attempt}, is not in the word!")
 
        except Exception as _error:
            print(_error)
 
        print(display_hangman(attempts))
        print(' '.join(char_ if char_ in guessed_letters else "_" for char_ in word_as_list))
        print("\n")
 
    if guessed:
        print(f"You guessed the word > {word} < you win!")
    else:
        print(f"You ran out of attempts. The word was {word}.")
 
def display_hangman(attempt_number):
    return stages[attempt_number]
 
 
if __name__ == "__main__":
    word = get_word()
    play(word)
    keep_playing = True
 
    while keep_playing:
        try:
            selected_option = input("play again? (Y/N): \n").upper()
            if selected_option == "Y":
                word = get_word()
                play(word)
 
            elif selected_option == "N":
                print("Game exiting.")
                keep_playing = False
 
            else:
                raise InvalidOptionError(f"{selected_option} is invalid, please input Y or N to continue.")
 
        except Exception as e:
            print(e)
 