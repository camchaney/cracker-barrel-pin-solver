# Cracker Barrel pin game
import numpy as np

# Initialize matrices
board0 = np.array([	[0,2,2,2,2],
					[1,1,2,2,2],
					[1,1,1,2,2],
					[1,1,1,1,2],
					[1,1,1,1,1]])
dir0 = 0 							# trigger direction using if statement
pin0 = 0  						# index of avaialable pins
boards = []
dirs = []
pins = []

# Fill out first element of matrices
boards.append(board0)
dirs.append(dir0)
pins.append(pin0)


n = 14				# initial number of pins

while n > 1:
	pchange = 0
	# use current board and selections
	curr_board = boards[-1]
	curr_dir = dirs[-1]
	curr_pin = pins[-1]

	# Check if there are more pins to try or not
	if curr_pin > (n - 1):
		# delete current branch and go back
		del boards[-1],dirs[-1],pins[-1]
		if dirs[-1] < 5:
			# if there are still moves to do on last pin selection
			dirs[-1] += 1
			continue
		else:
			pins[-1] += 1
			dirs[-1] = 0
			continue

	# find pin index
	(r,c) = np.where(curr_board == 1)
	r = r[curr_pin]
	c = c[curr_pin]

	# try move in certain direction
	for i in range(curr_dir,6):
		if i == 0:
			#print("i = 0")
			if r < 2:
				continue
			if (curr_board[r-1,c]==1) and (curr_board[r-2,c]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0 			# pin to move
				boards[-1][r-1,c] = 0   		# pin to hop		
				boards[-1][r-2,c] = 1 		# new pin placement
				dirs.append(0)
				pins.append(0)
				break
			else:
				continue
		if i == 1:
			if c > 2:
				continue
			if (curr_board[r,c+1]==1) and (curr_board[r,c+2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0
				boards[-1][r,c+1] = 0
				boards[-1][r,c+2] = 1
				dirs.append(0)
				pins.append(0)
				break
			else:
				continue
		if i == 2:
			if c > 2 or r > 2:
				continue
			if (curr_board[r+1,c+1]==1) and (curr_board[r+2,c+2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0
				boards[-1][r+1,c+1] = 0
				boards[-1][r+2,c+2] = 1
				dirs.append(0)
				pins.append(0)
				break
			else:
				continue
		if i == 3:
			if r > 2:
				continue
			if (curr_board[r+1,c]==1) and (curr_board[r+2,c]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0
				boards[-1][r+1,c] = 0
				boards[-1][r+2,c] = 1
				dirs.append(0)
				pins.append(0)
				break
			else:
				continue
		if i == 4:
			if c < 2:
				continue
			if (curr_board[r,c-1]==1) and (curr_board[r,c-2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0
				boards[-1][r,c-1] = 0
				boards[-1][r,c-2] = 1
				dirs.append(0)
				pins.append(0)
				break
			else:
				continue
		if i == 5:
			if r < 2 or c < 2:
				# Progress pin
				pins[-1] += 1
				dirs[-1] = 0
				# print(pins[-1])
				continue
			if (curr_board[r-1,c-1]==1) and (curr_board[r-2,c-2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				boards.append(np.copy(curr_board))
				boards[-1][r,c] = 0
				boards[-1][r-1,c-1] = 0
				boards[-1][r-2,c-2] = 1
				dirs.append(0)
				pins.append(0)
				break			# end of direction choices
			else:
				# Progress pin
				pins[-1] += 1
				dirs[-1] = 0


	n = sum(sum(boards[-1]==1))		# number of pins on board
	# if not pchange and len(boards) > 2:
	# 	#print(f"n = {n}")
	# 	print(f"moves = {len(boards)}")
	# 	print(f"(r,c) = ({r},{c})")
	# 	print(f"pin = {curr_pin}")
	# 	print(f"dir = {dirs[-2]}")
	# 	print(boards[-1])
	# 	#print(boards)


for board in boards:
	print(board )