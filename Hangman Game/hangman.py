import random
#This is the first while loop that allows the game to continue indefinitely
while True:
  while True:
    #User inputs their name to be greated
    try:
      username = input("What is your name? >> ")
      username = username.strip()
      
      #Prevents user from leaving name field blank
      if username == "":
        print("You can't leave this field blank!")
      else:
        print(f"Welcome to hangman, {username}!")
        break
    except ValueError:
      quit()

  #Python opens the file with our word list
  with open("word_list.txt", "r") as file:
    words = file.readlines()
    words = [word.strip() for word in words]
    random_word = random.choice(words)

  #Defines the variables we'll reuse the whole game
  secret_word = list(random_word)
  display_word = ["_ "] * len(secret_word)
  clean_word = "".join(display_word)
  tries = 7

  print(f"You have {tries} tries to guess the word: {clean_word}")

  #Main loop for the game
  while "_ " in display_word:
    user_guess = input("Guess a letter: ")

    #Prevents the user from guessing more than I letter at a time
    if len(user_guess) > 1:
      print("Please only guess one letter at a time.")
      continue

    #Replaces a blank in the word with user's correctly guessed letter
    if user_guess in secret_word:
      indexes = [] 
      for i, char in enumerate(secret_word):  
        if char == user_guess:  
          indexes.append(i)
        for x in indexes:
            display_word[x] = user_guess
      print("".join(display_word))

    #Tells user guess was wrong and reduces their score
    elif user_guess not in secret_word:
      tries -= 1
      print(f"Sorry, that was wrong! ({tries} tries remaining)")
      print("".join(display_word))
      if tries == 0:
        break

  #Ends the game when user correctly guesses all letters
  if "_ " not in display_word:
    print("Congratulations! You won this round.")

  #Ends the game when user runs out of tries
  if tries == 0:
    print("You lost this round. Better luck next time!")
    print(f"Oh! And the word was {random_word}")

  #Asks the user if they'd like to play again. Any input that is not y ends the program
  play_again = input("Would you like to play again (y/n)? ")
  
  if play_again.lower() == "y":
    print("Let's play again!")
    continue
  else:
    print("Thanks for playing!")
    break 
