import random

# List of words for the game
words = ["happiness", "relaxation", "mindfulness", "positivity", "wellness"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_game():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations, you guessed the word!")
            break

    if "_" in display:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")
    
if __name__ == "__main__":
    play_game()
