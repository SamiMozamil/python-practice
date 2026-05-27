import random

# ==========================================
# 1. Unique Character Finder (Problem 3)
# ==========================================
def has_unique_characters(text):
    # A set only keeps unique elements.
    # If the length of the set matches the original string, all characters are unique.
    return len(set(text)) == len(text)


# ==========================================
# 2. Number Guessing Game (Problem 4)
# ==========================================
def play_guessing_game():
    # Randomly select a number between 1 and 100
    target_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    # Loop until the user finds the number
    while True:
        user_input = input("Enter your guess: ").strip()
        
        # Handle invalid non-numeric inputs gracefully
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
            continue
            
        # Handle numbers outside the valid range gracefully
        if guess < 1 or guess > 100:
            print("Out of range! Please enter a number between 1 and 100.")
            continue
            
        # Provide feedback and check the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            # Congratulate the player and exit
            print(f"Congratulations! You guessed the correct number: {target_number}!")
            break

# ==========================================
# Execution Block
# ==========================================
if __name__ == "__main__":
    # Test the Unique Character Finder
    print("--- Testing Unique Character Finder ---")
    print(has_unique_characters("abcdef"))  # Expects True
    print(has_unique_characters("hello"))   # Expects False
    print()

    # Start the Guessing Game
    print("--- Starting Guessing Game ---")
    play_guessing_game()
