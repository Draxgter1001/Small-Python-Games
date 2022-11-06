import random

random_num = random.randrange(-1, 20)
tries = 3

print('Welcome to my Guess the Number Game')
play = input('To play please enter y otherwise enter any character to quit: ')

if play != 'y':
    quit()

print('You only have 3 tries, Good Luck!\n')

while tries > 0:
    try:
        user_number = int(input('Enter your number: '))
    except ValueError:
        print('The value that you have entered is not a number, please try again.')
        continue

    if user_number != random_num:
        tries -= 1
        if user_number > random_num and tries > 0:
            print('The number you have entered was too high!')
            print('You still have', tries, ' tries left.')
        elif user_number < random_num and tries > 0:
            print('The number you have entered was too low!')
            print('You still have', tries, ' tries left.')
    elif user_number == random_num:
        print('\nNice you won! You guessed the random number.')
        break
    
if tries <= 0:
    print('Sorry you lost! Better luck next time')
        
    
    

