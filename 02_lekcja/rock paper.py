import random
rounds_counter = int(input('How many rounds do you want to play? '))
game = ['rock', 'paper', 'scissors']
cpu = random.choice(game)
cpu_win = 0
player_win = 0
draw_games = 0

player = input('Pick one: "rock", "paper" or "scissors": ')
print('AI has choosen', cpu, end='. ')

for _ in range(rounds_counter - 1):
    cpu = random.choice(game)
    player = input('Pick one: "rock", "paper" or "scissors": ')
    print('AI has choosen', cpu, end='. ')
    if player == cpu:
        draw_games += 1
        print('Tie!')
    elif player == 'rock':
        if cpu == 'scissors':
            player_win += 1
            print('You win!')
        else:
            cpu_win += 1
            print('You lose!')
    elif player == 'paper':
        if cpu == 'rock':
            player_win += 1
            print('You win!')
        else:
            cpu_win += 1
            print('You lose!')
    elif player == 'scissors':
        if cpu == 'paper':
            player_win += 1
            print('You win!')
        else:
            cpu_win += 1
            print('You lose!')

    if player_win > cpu_win:
        print('You won', player_win, 'games, to', cpu_win, 'CPU wins.')
    elif cpu_win > player_win:
        print('You lost! CPU won', cpu_win, 'times and you won', player_win, 'wins.')
    else:
        print('Draw! You both won', player_win, 'times.')

