import random

# List of words for the game
words = ["python", "java", "hangman", "programming", "computer", "software"]

def select_random_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with guessed letters or underscores for unguessed letters
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Set the maximum incorrect guesses allowed

    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, {guess} is not in the word.")

        if all([letter in guessed_letters for letter in word]):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

# Run the hangman game
if __name__ == "__main__":
    hangman()
