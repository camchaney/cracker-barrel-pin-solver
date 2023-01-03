# Cracker Barrel pin game
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math

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

# Output --------------------------------------------------------------------
# Simple terminal output
i = 0
for board in boards:
	print(pins[i])
	print(board)
	i += 1

# Plot initialization
l = len(boards)  						# num sub-plots (number of moves)
fig, ax = plt.subplots(1, 1, sharex=True)
#fig1.add_subplot(1, 1, 1)
# for i in range(2, l + 1):
#     fig1.add_subplot(l, 1, i)

# Make blank board
blank_x = np.array([2.0,
		1.5,2.5,
		1.0,2.0,3.0,
		0.5,1.5,2.5,3.5,
		0.0,1.0,2.0,3.0,4.0])
blank_y = np.array([4.0,
		3.0,3.0,
		2.0,2.0,2.0,
		1.0,1.0,1.0,1.0,
		0.0,0.0,0.0,0.0,0.0])
blank_y = blank_y * (math.sqrt(3)) / 2
	
(r,c) = np.where(boards[0] != 2)		# rows and columns of actual board pieces


x = []
y = []
for i in range(l):
	x_temp = []
	y_temp = []
	#p = 0
	for j in range(15):
		if boards[i][r[j],c[j]] == 1:
			# Filling in pins
			x_temp.append(blank_x[j])
			y_temp.append(blank_y[j])
			# # Marking pin to move
			# if pins[i] == p:
			# 	x_pin = blank_x[j]
			# 	y_pin = blank_y[j]
			# p += 1
	x.append(x_temp)
	y.append(y_temp)

# Initialize plot
ind = 0
[plot_board] = ax[0].plot(blank_x,blank_y)
[plot_pins] = ax[0].plot(x[ind],y[ind])
[plot_move] = ax[0].plot(x[ind][pins[ind]],y[ind][pins[ind]])
#ax[2].set_title(f"Motor Plotting")
#ax[i].set_xlabel('Time (s)')
#ax[i].set_ylabel('Motor Command (pwm)')
#ax[i].legend()

def moveForward(val):
	global ind
	if ind < len(x):
		ind += 1
		#ax[0].scatter(blank_x,blank_y,)
		plot_pins.set_xdata(x[ind])
		plot_pins.set_ydata(y[ind])
		plot_move.set_xdata(x[ind][pins[ind]])
		plot_move.set_ydata(y[ind][pins[ind]])
		return ind

def moveBack(val,ind):
	#global ind
	if ind > 0:
		ind -= 1
		#ax[0].scatter(blank_x,blank_y,)
		ax[0].scatter(x[ind],y[ind])
		ax[0].scatter(x[ind][pins[ind]],y[ind][pins[ind]])
		return ind

# Defining buttons and their functionality
axes = plt.axes([0.81, 0.000001, 0.1, 0.075])
bforward = Button(axes, '>',color="yellow")
bforward.on_clicked(moveForward)

print(pins)
plt.show()