import random


def guessing_game():
    print('Welcome to our number guessing game')
    range_input = input('Please fill out the number range in this format (A-B): ')

    if '-' not in range_input:
        print('Invalid range format. Please use the format (A-B).')
        return

    start_number, end_number = range_input.split('-')

    if not start_number.isdigit() or not end_number.isdigit():
        print('Invalid numbers. Please enter valid integers.')
        return

    start_number = int(start_number)
    end_number = int(end_number)

    random_number = random.randint(start_number, end_number)
    print(f"The random number is between {start_number} and {end_number}")

    game_end = False
    guess_count = 0

    while not game_end:
        user_input = input('Guess the number: ')

        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue

        user_number = int(user_input)
        guess_count += 1

        if user_number < random_number:
            print('Too low')
        elif user_number > random_number:
            print('Too high')
        else:
            print(f'Correct!!! You win! It took you {guess_count} guesses.')
            game_end = True

    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        guessing_game()
    else:
        print('You have exited the game. Thanks for playing!')


guessing_game()



