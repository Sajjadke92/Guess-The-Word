# Import the random module to use for random selections
import random
# List of word categories
file_categories = ['Sports', 'Car Brands', 'Cities', 'Clothing Brands', 'Countries', 'Foods']

rematch = True    # Flag to control rematch loop
restart = True    # Flag to control restart loop

# Main loop that continues based on the rematch and restart
while rematch == True or restart == True:
 if restart == True or rematch == False:  # For starting a new game , not a rematch
    player = input('write your name to play...')  # Get the player's name
    if player == 'stop':  # To stop the game
        break
 else:
     print(f'\nlets play again {player}')  # Message for rematch

 def choose_random_file():  # Function to choose a random category file
    file = random.choice(file_categories)  # Choose a random category from the list
    return file
 file_name = choose_random_file()  # To store the chosen file name

# Function to choose a random word from the chosen category file
 def choose_word():
    with open(file_name+'.txt', 'r') as file:  # Open the category file
        words_list = file.read().split()     # Read and split words into a list
        return random.choice(words_list)     # Choose a random word from the list

 word = choose_word().lower()  # Get a random word and convert it to lowercase

 def change_word():   # Function to change the original word to underscores instead of any letter in word as a blank
     return ['_'] * len(word)  # Create a list of underscores of the same length as the word

 hidden_word = change_word()

 # Create a list of letters of the chosen word
 word_letter_list = []
 for letter in word:
      word_letter_list.append(letter)

 # Print the initial game information
 print(f'''\n Guess the word, letter by letter\n If you make 5 wrong guesses, you lose! 
 You can also guess the complete word\n Tips : The word is about {file_name} and has {len(word)} letters\n 
 lets start ;)\n''')
 print(''.join(hidden_word))

 # Function to check the guessed letter with any letter in word and replace it
 def player_guess(guess):
    j = 0
    while j < len(word):
        if word_letter_list[j] == guess:
            hidden_word[j] = guess       # Reveal the guessed letter in the hidden word
        j += 1
    return hidden_word

 win = False  # Flag to check if the player has won
 Counter = 0          # Counter for wrong guesses

 # Loop to get the guesses and check them till the number of wrong guesses reach to 5 or the player guess the word
 while Counter != 5:
     guess = input('guess a letter: ').lower()   # Get the player's guess

     # Set win flag if the player guesses the word and break the loop
     if player_guess(guess) == word_letter_list or guess == word:
         win = True
         break

     # Print the updated hidden word if the player guesses one of the letters in the letter list of the word
     elif guess in word_letter_list:
         print(''.join(player_guess(guess)))

     else:  # Increment the number of wrong guesses
      Counter += 1
     print('wrong guesses: ', Counter)

 # Print the result of the game
 if win:    # If win is True , it means the player has won
    print(f'heeey we have a winner here\n Congratulations, {player}')
 else:      # If win is False , it means the player has lost
    print(f'\nyou lose {player} :( The word was << {word} >>')

 # Ask the player if they want to play again
 play_again = input('\nPlay Again? Yes/No  ').lower()
 if play_again == 'no' or play_again == 'n':
    print(f'Good Bye {player}\n')
    rematch = False  # Set rematch flag to False,because the player do not want to play again
    restart = True   # Set restart flag to True,to start the new game for other player
 elif play_again == 'yes' or play_again == 'y':
     rematch = True   # Set rematch flag to True,because the player want to play again
     restart = False  # Set restart flag to False,because it is not a new game
 else:      # This is for other inputs when the player answer to play again question
    print('I take this as no! >( \n Good Bye...!\n')
    rematch = False
    restart = True
