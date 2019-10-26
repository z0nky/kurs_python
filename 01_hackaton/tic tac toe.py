board = [['   ', ' 1 ', ' 2 ', ' 3 '],
         [' A ', ' . ', ' . ', ' . '],
         [' B ', ' . ', ' . ', ' . '],
         [' C ', ' . ', ' . ', ' . ']]

moves = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

for rows in board:
    for val in rows:
        print(val, end=' ')
    print()


player_m = input('Podaj komórkę, w którą zagrywasz krzyżyk: ').upper()
if len(player_m) != 2:
    print("\nYou need to tell me where you want to put cross!"
          "For example \"A1\" or \"C3\"")
if player_m in moves:
    moves.remove(player_m)
    first = player_m[0]
    second = player_m[1]
    print(first)
    print(second)
else:
    print('move not available')
print(len(player_m))
print(moves)
#print(board)
