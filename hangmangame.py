wrong_guesses = [
    "",
    "________",
    "| | ",
    "| 0 ",
    "| /|\\ ",  
    "| / \\ ",  
    "| "
]

word = "cat"
score_board = ['__'] * len(word)
win = False
stage = 0

print('Welcome to Hang Man')
print((' '.join(score_board)))
print('\n'.join(wrong_guesses[0:stage + 1]))

while stage < len(wrong_guesses) - 1:
    print('\n')
    guess = input("Guess a letter: ")
    
    # Check if the guess is a single letter and is in the word
    if len(guess) == 1 and guess in word:
        # Update the score_board with the correct guess
        for i in range(len(word)):
            if word[i] == guess:
                score_board[i] = guess
        
        # Check for a win
        if '__' not in score_board:
            print((' '.join(score_board)))
            print('You win! The word was:', word)
            win = True
            break
    else:
        # Incorrect guess, increment stage and show the next part of the hangman
        stage += 1
        
    print((' '.join(score_board)))
    print('\n'.join(wrong_guesses[0:stage + 1]))

if not win:
    print('You lose! The word was:', word)