print('Welcome to Game!') # Welcome message

# Initialize variables
lives = 3
answer = 150

# Loop forever
while True:
    question = int(input('What is 100 + 50?: '))
    
    # Check if answer is correct
    if question == answer:
        print('You are correct!')
        break
    else:
        lives -= 1
        print(f'Incorrect, You have {lives} left')
        if lives == 0:
            print('You lose')
            break
        
        
