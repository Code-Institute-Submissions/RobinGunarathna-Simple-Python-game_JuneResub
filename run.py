import random
import warnings
from constants import stage_dictionary as stages, word_list

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
        current_attempt = input("Guess a letter or a word: \n").upper()
        if current_attempt.isdigit():
            print(f"Numbers aren't allowed, try again.")
            continue

        if not is_word(current_attempt):

            if current_attempt in guessed_letters or current_attempt in failed_attempts:
                attempts += 1
                print(f"You already inputted {current_attempt}")

            elif current_attempt not in word:
                print(f"{current_attempt}, is not in the word!")
                attempts += 1
                failed_attempts.append(current_attempt)

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
                print(f"You already tried the word {current_attempt}.")
            else:
                print(f"{current_attempt} is not the word.")
                attempts += 1
                failed_attempts.append(current_attempt)

        print(display_hangman(attempts))
        print(' '.join(char_ if char_ in guessed_letters else "_" for char_ in word_as_list))
        print("\n")

    if guessed:
        print(f"You guessed the word > {word} < you win!")
    else:
        print(f"You ran out of attempts. The word was {word}. Try again?")

def display_hangman(attempt_number):
    return stages[attempt_number]


if __name__ == "__main__":
    word = get_word()
    play(word)
    keep_playing = True

    while keep_playing:
        selected_option = input("play again? (Y/N): \n").upper()
        if selected_option == "Y":
            word = get_word()
            play(word)

        elif selected_option == "N":
            print("Game exiting.")
            keep_playing = False

        else:
            print(f"{selected_option} is invalid, please input Y or N to continue.")