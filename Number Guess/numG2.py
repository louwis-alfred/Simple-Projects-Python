import random

# Initialize variable
attempt = 0


top_of_range = int(input('Type a number: ')) 
random_number = random.randint(1, top_of_range)

try:
    while True:
        # Get user guess
        guess = int(input("Make a guess: "))
        # Check the condition if Right number is higher or lower
        if guess > random_number:
            print('Lower')
            attempt += 1
        elif guess < random_number:
            print('Higher')
            attempt += 1
        elif guess == random_number:
            print('You nailed it!')
            # Check the singular and plural form of "Attempts"
            if attempt > 1:
                print(f'You have {attempt} attempts')
            else:
                print(f'You have {attempt} attempt')
            break
except ValueError:
    print('Please type a number')
    


