# Cracker Barrel pin game
import numpy as np

# Initialize matrices
path0 = np.array([[0,2,2,2,2],
				[1,1,2,2,2],
				[1,1,1,2,2],
				[1,1,1,1,2],
				[1,1,1,1,1]]);
move0 = 0 							# trigger move using if statement
pin0 = 0  						# index of avaialable pins
paths = []
moves = []
pins = []

# Fill out first element of matrices
paths.append(path0)
moves.append(move0)
pins.append(pin0)


n = sum(sum(path0))

while n > 1:
	# use current path map
	path0 = paths[-1]
	move0 = moves[-1]
	pin0 = pins[-1]

	# find pin index
	(r,c) = np.where(path0 == 1)
	r = r[pin0]
	c = c[pin0]

	# try move
	for i in range(move0,6):
		if i == 0:
			if r < 2:
				continue
			if (path0[r-1,c]==1) and (path0[r-2,c]==0):
				# make and fill new path map
				paths.append(path0)
				paths[-1][r,c] = 0
				paths[-1][r-1,c] = 0
				paths[-1][r-2,c] = 1
				# update move number
				moves[-1] = i
				break
			else:
				continue
		if i == 1:
			if c > 2:
				continue
			if (path0[r,c+1]==1) and (path0[r,c+2]==0):
				# make and fill new path map
				paths.append(path0)
				paths[-1][r,c] = 0
				paths[-1][r-1,c] = 0
				paths[-1][r-2,c] = 1
				# update move number
				moves[-1] = i
				breaks



	# setup for next move
	path0 = 
	n = sum(sum(path0))