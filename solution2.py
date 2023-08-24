import random

rand_nr = int(random.randrange(1, 10))
guess = 0

while guess == 0:
    input_user = int(input('Guess a number between 1 and 10: '))
    
    if input_user == rand_nr:
        guess = 1
        print('Well guessed! The number was:', input_user)
    elif input_user > rand_nr:
        print('Too big')
    elif input_user < rand_nr:
        print('Too small')
    else:
        continue
        