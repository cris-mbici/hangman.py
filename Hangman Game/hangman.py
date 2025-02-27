import random  # Import random for word selection

# Ask for the player's name, ensuring it's not empty
while True:
    try:
        username = input("What is your name? >> ").strip()
        if username:
            print(f"Welcome to hangman, {username}!")
            break
        print("You can't leave this field blank!")
    except ValueError:
        quit()

# Main game loop
while True:
    # Load words from file and pick one at random
    with open("word_list.txt", "r") as file:
        words = [word.strip() for word in file.readlines()]
        random_word = random.choice(words)

    secret_word = list(random_word)
    display_word = ["_ "] * len(secret_word)
    tries = 7

    print(f"You have {tries} tries to guess the word: {''.join(display_word)}")

    # Letter guessing loop
    while "_ " in display_word and tries > 0:
        user_guess = input("Guess a letter: ")
        if len(user_guess) > 1:
            print("Please only guess one letter at a time.")
            continue

        if user_guess in secret_word:
            for i, char in enumerate(secret_word):
                if char == user_guess:
                    display_word[i] = user_guess
            print("".join(display_word))
        else:
            tries -= 1
            print(f"Sorry, that was wrong! ({tries} tries remaining)")
            print("".join(display_word))

    # Display game outcome
    if "_ " not in display_word:
        print("Congratulations! You won this round.")
    else:
        print(f"You lost this round. The word was {random_word}.")

    # Play again prompt
    if input("Would you like to play again (y/n)? ").strip().lower() != "y":
        print("Thanks for playing!")
        break
