import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12334
server.bind((host, port))
server.listen(5)

csoc, caddr = server.accept()

############ Logic for Game ############ 
board = ['-' for _ in range(9)]

print("The board is numbered like this:")
for i in range(3):
	for j in range(3):
		print(i * 3 + j,end = " ")
	print()

print("------------------------------------------------")

def check_win(board, player):
	win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
						(0, 3, 6), (1, 4, 7), (2, 5, 8),
						(0, 4, 8), (2, 4, 6))
	for row in win_conditions:
		if board[row[0]] == player and board[row[1]] == player and board[row[2]] == player:
			# print(row)
			return True
	return False


def draw_board(board):
    """
    Prints the current state of the game board for visualization.
    """
    for i in range(3):
        for j in range(3):
            print(board[i * 3 + j], end=" ")
        print()

def empty_spaces(board):
	cnt = 0
	for sp in board:
		if sp == '-':
			cnt = cnt + 1
	return cnt
	
print("Player 1, please enter X")

print("Player 2, please enter O")




t = 1
draw = True

while empty_spaces(board):
	print("Current board:")
	draw_board(board)
	
	player = 'X'
	if(t == 0):
		player = 'O'
	if(player=='O'):
		msg1="Turn for player O:\n"
		csoc.send(msg1.encode('utf-8'))
	print(f"Turn for player {player}")
	
	
	move = -1
	
	while (True):
		if(player=='O'):
			msg2="Enter your move (0 - 8):\n"
			csoc.send(msg2.encode('utf-8'))
			rsp1=csoc.recv(1024).decode('utf-8')
			print(rsp1)
			move=int(rsp1)
		else:
			move = int(input("Enter your move (0 - 8):\n"))
		# move = int(input("Enter your move (0 - 8) : "))
			
		if((0 <= move and move < 9)):
			if board[move] != '-':
				print("Wrong move! Its not an empty space")
			else:
				break
		else:
			print("Invalid move!! Please enter a valid one")
			
	board[move] = player
	
	if(check_win(board,player)):
		draw_board(board)
		print(f"Player {player} has won the match!")
		draw = False
		break
	t = t ^ 1
	
if draw:
	print("Match drawn!")
csoc.send(b"end")
############ Logic for Game Ended ############ 


