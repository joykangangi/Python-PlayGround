import random

answers_list = ['rock', 'paper', 'scissors']
random.shuffle(answers_list)
user_guess = input('Choose: rock, paper or scissors?')
computer_guess = random.choice(answers_list)

if user_guess == computer_guess:
    print('It is a tie Try Again')
    random.shuffle(answers_list)
    user_guess = input('Choose: rock, paper or scissors?')
elif user_guess != computer_guess:
    if user_guess == 'rock' and computer_guess == 'paper':
        result = 'Oh dear, You lost to paper, Shikamana!'
    elif user_guess == 'rock' and computer_guess == 'scissors':
        result = 'Yaay, You won against scissors!'
    elif user_guess == 'paper' and computer_guess == 'rock':
        result = 'Yaay, you won against rock!'
    elif user_guess == 'paper' and computer_guess == 'scissors':
        result = 'Sorry, you lost to scissors!, Chop!Chop!Chop!'
    elif user_guess == 'scissors' and computer_guess == 'rock':
        result = 'Oopsy, you lost to rock, Kong!Kong!Kong!'
    elif user_guess != computer_guess and user_guess == 'scissors' and computer_guess == 'paper':
        result = 'Yaay, you won against paper 💰!'
else:
    result = 'Wrong input'

print(result)
