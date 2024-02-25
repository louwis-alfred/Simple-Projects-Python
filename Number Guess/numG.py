import random

attempt = 0
r = random.randrange(1,11)

while True:
    answer = int(input('Guess a number between 1-10: '))
    if answer != r:
        attempt += 1
        print('Wrong')
    else:
        print(f'You are correct! you guess that {attempt}')
        break