import pprint
# Part 1
with open('input.txt') as input_file:
	h = (0,0)
	t = (0,0)
	visited = [h]
	for row in input_file:
		direction, count = row.split(' ')
		count = int(count)
		for _ in range(count):
			x, y = h
			if direction == "U":
				h = (x - 1, y)
			elif direction == "D":
				h = (x + 1, y)
			elif direction == "R":
				h = (x, y + 1)
			elif direction == "L":
				h = (x, y - 1)

			h_x, h_y = h
			t_x, t_y = t

			if (abs(h_x - t_x) <= 1) and (abs(h_y - t_y) <= 1):
				visited.append(t)
				continue

			if h_x - t_x >= 1:
				# H is to the right of T
				if h_y - t_y == -2:
					# H is below T, Diagonal
					t = (t_x + 1, t_y - 1)
				elif h_y - t_y == -1:
					# H is below T, Diagonal
					t = (t_x + 1, t_y - 1)
				elif h_y - t_y == 0:
					# Straight left, move right
					t = (t_x + 1, t_y)
				elif h_y - t_y == 1:
					# Diagonal to left, move up and right
					t = (t_x + 1, t_y + 1)
				elif h_y - t_y == 2:
					# Diagonal to left, move up and right
					t = (t_x + 1, t_y + 1)
			elif h_x - t_x == 0:
				if h_y - t_y == -2:
					t = (t_x, t_y - 1)
				elif h_y - t_y == 2:
					t = (t_x, t_y + 1)
			elif h_x - t_x <= -1:
				# H is to the right of T
				if h_y - t_y == -2:
					# H is below T, Diagonal
					t = (t_x - 1, t_y - 1)
				elif h_y - t_y == -1:
					# H is below T, Diagonal
					t = (t_x - 1, t_y - 1)
				elif h_y - t_y == 0:
					# Straight left, move right
					t = (t_x - 1, t_y)
				elif h_y - t_y == 1:
					# Diagonal to left, move up and right
					t = (t_x - 1, t_y + 1)
				elif h_y - t_y == 2:
					# Diagonal to left, move up and right
					t = (t_x - 1, t_y + 1)
			visited.append(t)
	#print(visited)
	#print(len(set(visited)))

# Part 2
with open('input.txt') as input_file:
	knots = [(0,0) for x in range(10)]
	visited = [knots[0]]

	for row in input_file:
		direction, count = row.split(' ')
		count = int(count)

		for _ in range(count):
			x, y = knots[9]
			if direction == "U":
				knots[-1] = (x - 1, y)
			elif direction == "D":
				knots[-1] = (x + 1, y)
			elif direction == "R":
				knots[-1] = (x, y + 1)
			elif direction == "L":
				knots[-1] = (x, y - 1)

			for i in range(9):
				h_x, h_y = knots[9 - i]
				t_x, t_y = knots[8 - i]

				if (abs(h_x - t_x) <= 1) and (abs(h_y - t_y) <= 1):
					continue

				if h_x - t_x >= 1:
					# H is to the right of T
					if h_y - t_y == -2:
						# H is below T, Diagonal
						t = (t_x + 1, t_y - 1)
					elif h_y - t_y == -1:
						# H is below T, Diagonal
						t = (t_x + 1, t_y - 1)
					elif h_y - t_y == 0:
						# Straight left, move right
						t = (t_x + 1, t_y)
					elif h_y - t_y == 1:
						# Diagonal to left, move up and right
						t = (t_x + 1, t_y + 1)
					elif h_y - t_y == 2:
						# Diagonal to left, move up and right
						t = (t_x + 1, t_y + 1)
				elif h_x - t_x == 0:
					if h_y - t_y == -2:
						t = (t_x, t_y - 1)
					elif h_y - t_y == 2:
						t = (t_x, t_y + 1)
				elif h_x - t_x <= -1:
					# H is to the right of T
					if h_y - t_y == -2:
						# H is below T, Diagonal
						t = (t_x - 1, t_y - 1)
					elif h_y - t_y == -1:
						# H is below T, Diagonal
						t = (t_x - 1, t_y - 1)
					elif h_y - t_y == 0:
						# Straight left, move right
						t = (t_x - 1, t_y)
					elif h_y - t_y == 1:
						# Diagonal to left, move up and right
						t = (t_x - 1, t_y + 1)
					elif h_y - t_y == 2:
						# Diagonal to left, move up and right
						t = (t_x - 1, t_y + 1)
				knots[8-i] = t
			visited.append(knots[0])
	print(visited)
	print(len(set(visited)))