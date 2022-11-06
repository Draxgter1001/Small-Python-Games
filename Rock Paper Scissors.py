import random
user_score = 0
computer_score = 0

print('Beat the Computer in a Rock, Paper & Scissors game!\n')

def outcomes(user_input, computer_input):
    global user_score 
    global computer_score
    
    if user_input == 'rock' and computer_input == 'scissors':
        user_score += 1
        print('You Won!')  
    elif user_input == 'paper' and computer_input == 'rock':
        user_score += 1
        print('You Won!')
    elif user_input == 'scissors' and computer_input == 'paper':
        user_score += 1
        print('You Won!')
    else:
        computer_score += 1
        print('You Lost!')

    return True
    
while True:
    user_pick = input('Enter Rock/Paper/Scissors or enter Q to quit: ').lower()
    options = ['rock', 'paper', 'scissors']
    
    if user_pick == 'q':
        break
    elif user_pick not in options:
        print('The option you have entered is not valid.')
        continue

    computer_pick = options[random.randint(0, 2)]

    if outcomes(user_pick, computer_pick):
        continue

print('\nYour score:', user_score)
print('Computer Score:', computer_score)
print('\nThank you for playing')