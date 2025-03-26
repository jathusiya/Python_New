import random

number_to_guess = random.randint(1,100)

# user_input = input('Guess the number between 1 and 100: ')
# guess = int(user_input)
while True:
        try:
            guess = int(input('Guess the number between 1 and 100: '))

            if guess < number_to_guess:
                print('Too low!')
            elif guess > number_to_guess:
                print('Too high!')
            else:
                print('Congratualtion. You guessed the number.')
                break
        except ValueError:
            print('Please enter a valid number')


