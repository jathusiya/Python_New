import random

ROCK = 'r'
SCISSORS = 'S'
PAPER = 'P'

emojis = {ROCK:'🥊', SCISSORS:'✂️', PAPER :'📃'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock,paper or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    elif user_choice == 's' and computer_choice == 'p':
        print('You win')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        Should_Continue = input('Continue? (y/n): '.lower())
        if Should_Continue == 'n':
            break
        
play_game()