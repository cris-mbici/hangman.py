import random
while True:
  while True:
    try:
      username = input("What is your name? >> ")
      username = username.strip()  
      if username == "":
        print("You can't leave this field blank!")
      else:
        print(f"Welcome to hangman, {username}!")
        break
    except ValueError:
      quit()

  with open("word_list.txt", "r") as file:
    words = file.readlines()
    words = [word.strip() for word in words]
    random_word = random.choice(words)

  secret_word = list(random_word)
  display_word = ["_ "] * len(secret_word)
  clean_word = "".join(display_word)
  tries = 7

  print(f"You have {tries} tries to guess the word: {clean_word}")

  while "_ " in display_word:
    user_guess = input("Guess a letter: ")
    if len(user_guess) > 1:
      print("Please only guess one letter at a time.")
      continue
    if user_guess in secret_word:
      indexes = [] 
      for i, char in enumerate(secret_word):  
        if char == user_guess:  
          indexes.append(i)
        for x in indexes:
            display_word[x] = user_guess
      print("".join(display_word))
  
    elif user_guess not in secret_word:
      tries -= 1
      print(f"Sorry, that was wrong! ({tries} tries remaining)")
      print("".join(display_word))
      if tries == 0:
        break

  if "_ " not in display_word:
    print("Congratulations! You won this round.")

  if tries == 0:
    print("You lost this round. Better luck next time!")
    print(f"Oh! And the word was {random_word}")

  play_again = input("Would you like to play again (y/n)? ")
  
  if play_again.lower() == "y":
    print("Let's play again!")
    continue
  else:
    print("Thanks for playing!")
    break 