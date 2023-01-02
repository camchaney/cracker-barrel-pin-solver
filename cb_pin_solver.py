# Cracker Barrel pin game
import numpy as np

# Initialize matrices
path0 = np.array([	[0,2,2,2,2],
					[1,1,2,2,2],
					[1,1,1,2,2],
					[1,1,1,1,2],
					[1,1,1,1,1]])
dir0 = 0 							# trigger direction using if statement
pin0 = 0  						# index of avaialable pins
paths = []
dirs = []
pins = []

# Fill out first element of matrices
paths.append(path0)
dirs.append(dir0)
pins.append(pin0)


n = 14				# initial number of pins

while n > 1:
	pchange = 0
	# use current path map
	path0 = paths[-1]
	dir0 = dirs[-1]
	pin0 = pins[-1]

	# find pin index
	(r,c) = np.where(path0 == 1)
	r = r[pin0]
	c = c[pin0]

	# try move in certain direction
	for i in range(dir0,6):
		if i == 0:
			#print("i = 0")
			if r < 2:
				continue
			if (path0[r-1,c]==1) and (path0[r-2,c]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0 			# pin to move
				paths[-1][r-1,c] = 0   		# pin to hop		
				paths[-1][r-2,c] = 1 		# new pin placement
				break
			else:
				continue
		if i == 1:
			if c > 2:
				continue
			if (path0[r,c+1]==1) and (path0[r,c+2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0
				paths[-1][r,c+1] = 0
				paths[-1][r,c+2] = 1
				break
			else:
				continue
		if i == 2:
			if c > 2 or r > 2:
				continue
			if (path0[r+1,c+1]==1) and (path0[r+2,c+2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0
				paths[-1][r+1,c+1] = 0
				paths[-1][r+2,c+2] = 1
				break
			else:
				continue
		if i == 3:
			if r > 2:
				continue
			if (path0[r+1,c]==1) and (path0[r+2,c]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0
				paths[-1][r+1,c] = 0
				paths[-1][r+2,c] = 1
				break
			else:
				continue
		if i == 4:
			if c < 2:
				continue
			if (path0[r,c-1]==1) and (path0[r,c-2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0
				paths[-1][r,c-1] = 0
				paths[-1][r,c-2] = 1
				break
			else:
				continue
		if i == 5:
			if r < 2 or c < 2:
				# Progress dirs
				if pin0+1 < sum(sum(paths[-1]==1)):		# if there are still more pins
					# change pin
					pins[-1] += 1
					dirs[-1] = 0
					# print(pins[-1])
				else:									# if there are no more pins to try
					# delete current branch and go back
					del paths[-1],dirs[-1],pins[-1]
				continue
			if (path0[r-1,c-1]==1) and (path0[r-2,c-2]==0):
				# log changes
				dirs[-1] = i
				# make and fill new move
				paths.append(np.copy(path0))
				dirs.append(0)
				pins.append(0)
				paths[-1][r,c] = 0
				paths[-1][r-1,c-1] = 0
				paths[-1][r-2,c-2] = 1
				break			# end of direction choices
			else:
				# Progress dirs
				if pin0+1 < sum(sum(paths[-1]==1)):		# if there are still more pins
					pchange = 1
					# change pin
					pins[-1] += 1
					dirs[-1] = 0
					# print(f"pin after progress = {pins[-1]}")
				else:									# if there are no more pins to try
					# delete current branch and go back
					del paths[-1],dirs[-1],pins[-1]
					# print("After branch deletion:")
					# print(f"pin = {pins[-1]}")
					# print(f"dir = {dirs[-1]}")
					# print(paths[-1])


	n = sum(sum(paths[-1]==1))
	# if not pchange and len(paths) > 2:
	# 	#print(f"n = {n}")
	# 	print(f"moves = {len(paths)}")
	# 	print(f"(r,c) = ({r},{c})")
	# 	print(f"pin = {pin0}")
	# 	print(f"dir = {dirs[-2]}")
	# 	print(paths[-1])
	# 	#print(paths)



print(paths)