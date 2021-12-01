import random


def is_integer(nb: str) -> bool:
    if nb.isdigit() or nb.startswith('-') and nb[1:].isdigit():
        return True
    return False


print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n''')

mystery_number = random.randint(1, 100)
print(mystery_number)
current_game = True
attempts = 0
while current_game:
    input_user = input('What\'s your guess between 1 and 99?\n')
    attempts += 1
    if input_user == 'exit':
        print('Goodbye!')
        current_game = False
    elif not is_integer(input_user):
        print('That\'s not a number.')
    elif int(input_user) < 1 or int(input_user) > 99:
        print('The number must be between 1 and 99.')
    elif int(input_user) < mystery_number:
        print('Too low!')
    elif int(input_user) > mystery_number:
        print('Too high!')
    elif int(input_user) == mystery_number:
        if mystery_number == 42:
            print('The answer to the ultimate question of life,'
                  'the universe and everything is 42.')
        if attempts == 1:
            print('Congratulations! You got it on your first try!')
        else:
            print('Congratulations, you\'ve got it!\n'
                  'You won in {} attempts!'.format(attempts))
        current_game = False
