''' ROCK PAPER SCISSORS '''

import random, sys

print('ROCK, PAPER, SCISSORS !!!')

#These variables keep track of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True:
    print(f'{wins} Wins, {losses} Losses, and {ties} Ties!')
    while True:
        print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit.\n')
        move = input()
        if move == 'q':
            sys.exit()
        if move in 'rps':
            break
        print('\nType one of r, p, s, or q.\n')

    #Display what the player chose
    if move == 'r':
        print('ROCK vs ...')
    elif move == 'p':
        print('PAPER vs ...')
    elif move == 's':
        print('SCISSORS vs ...')

    #Display what the computer chose
    num = random.randint(1, 3)
    if num == 1:
        comp = 'r'
        print('ROCK')
    elif num == 2:
        comp = 'p'
        print('PAPER')
    elif num == 3:
        comp = 's'
        print('SCISSORS')

    #Display and record the wins, losses, and ties
    if move == comp:
        print('It is a tie')
        ties += 1
        
    elif move == 'r' and comp == 's':
        print('You win!')
        wins += 1
    elif move == 's' and comp == 'p':
        print('You win!')
        wins += 1
    elif move == 'p' and comp == 'r':
        print('You win!')
        wins += 1
        
    elif move == 's' and comp == 'r':
        print('You lose!')
        losses += 1
    elif move == 'p' and comp == 's':
        print('You lose!')
        losses += 1
    elif move == 'r' and comp == 'p':
        print('You lose!')
        losses += 1










        
