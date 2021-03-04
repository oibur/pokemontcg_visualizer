import random, sys
#Rock,Paper,Scissor game I moded to be pokemon themed. 


print('CHARMANDER, SQUIRTLE, BULBASAUR \n Charmander(fire) beats Bulbasaur(grass) \n Bulbasaur(grass) beats Squirtle(water) \n Squirtle(water) beats Charmander(fire)')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (c)harmander (s)quirtle (b)ulbasaur or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'c' or playerMove == 's' or playerMove == 'b':
            break # Break out of the player input loop.
        print('Type one of c, s, b, or q.')

    # Display what the player chose:
    if playerMove == 'c':
        print('CHARMANDER versus...')
    elif playerMove == 's':
        print('SQUIRTLE versus...')
    elif playerMove == 'b':
        print('BULBASAUR versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'c'
        print('CHARMANDER')
    elif randomNumber == 2:
        computerMove = 's'
        print('SQUIRTLE')
    elif randomNumber == 3:
        computerMove = 'b'
        print('BULBASAUR')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'c' and computerMove == 'b':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'c':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'b' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'c' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'b':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'b' and computerMove == 'c':
        print('You lose!')
        losses = losses + 1