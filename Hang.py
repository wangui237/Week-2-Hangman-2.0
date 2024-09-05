import random


words = [
    'iteration', 'methodolody', 'encapsulation', 'programming', 'interface', 'module',
    'framework', 'algorithm', 'debugging', 'polymorphism', 'recursion', 'algorithm'
]

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def hangman_game():
    word = random.choice(words)
    guessed_letters = set()
    failed_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while failed_attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            failed_attempts += 1
            print(f"Incorrect guess. You have {max_attempts - failed_attempts} attempts left.")
        
        
        current_display = display_word(word, guessed_letters)
        print(current_display)

        
        if '_' not in current_display:
            print("Congratulations! You've guessed the word.")
            break
    else:
        
        print(f"Game over. The word was '{word}'. You Lost.")

if __name__ == '__main__':
    hangman_game()