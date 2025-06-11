import random

options = ('rock', 'paper', 'scissors')

user_wins = 0
computer_wins = 0
rounds = 1

while True:
    
    print('*'*10)
    print('Round', rounds)
    print('*'*10)
    print('User wins:', user_wins)
    print('Computer wins:', computer_wins)

    user_option = input('Rock, paper or scissors -> ')
    user_option = user_option.lower()

    if user_option not in options:
        print('Invalid option')
        continue

    computer_option = random.choice(options)

    rounds += 1

    print('User option ->', user_option)
    print('Computer option ->', computer_option)

    if user_option == computer_option:
        print('It\'s a tie')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('User wins!')
            user_wins += 1
        else:
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'scissors':
            print('Computer wins!')
            computer_wins += 1
        else:
            print('User wins!')
            user_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('User wins!')
            user_wins += 1
        else:
            print('Computer wins!')
            computer_wins += 1

    if user_wins == 3:
        print('The user is the winner!')
        break

    if computer_wins == 3:
        print('The computer is the winner!')
        break