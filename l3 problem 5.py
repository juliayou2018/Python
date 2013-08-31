print('Please think of a number between 0 and 100!')
low = 0
high = 100
finished = False

while not finished:
    guess = (low + high)/2
    print('Is your secret number ' + str(guess) + '?')
    user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    elif user_input == 'c':
        finished = True
    else:
        print('Sorry, I did not understand your input.')
        
print('Game over. Your secret number was: ' + str(guess))
