# create a greeting
# create your word list
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word

import random, string

print("Welcome to Hangman!")

wordlist = ["red","blue","green","purple","hacker","bounty","testing"]
char_available = string.ascii_lowercase
secret = random.choice(wordlist)
display_word =list("_"*len(secret))
print(display_word)

not_found = 0
game_over = False
while not game_over:
    guess = input("Letter guess: ").lower()
    if len(guess) > 1:
        print("Guess must be 1 character!")
        continue

    for i in range(0,len(secret)):
        if guess == secret[i]:
            display_word[i] = guess
            print(display_word)
        elif guess != secret[i] and i == len(secret) - 1 :
            not_found += 1 
    
    if "_" not in display_word:
        print(f"WORD FOUND")
        game_over = True
    if not_found == 5:
        print("YOU LOSE")
        game_over = True

