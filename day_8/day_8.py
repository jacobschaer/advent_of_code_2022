import pprint
from math import prod
with open('input.txt') as input_file:
	tree_heights = []
	for line in input_file:
		tree_heights.append(list(map(int, line.strip())))
	#print(tree_heights)

	TOP = 0
	LEFT = 1
	BOTTOM = 2
	RIGHT = 3

	# Part 1: WE can do better than bruteforce by keeping track of two directions as we iterate
	# forward and backwards - could optimize for the edges better but less convenient
	max_heights = []
	for i in range(len(tree_heights)):
		row = []
		for j in range(len(tree_heights[i])):
			row.append([-1] * 4)
		max_heights.append(row)

	# Fill in Top/Left
	for i in range(1, len(tree_heights)):
		for j in range(1, len(tree_heights[i])):
			max_heights[i][j][TOP] = max(max_heights[i - 1][j][TOP], tree_heights[i - 1][j])
			max_heights[i][j][LEFT] = max(max_heights[i][j - 1][LEFT], tree_heights[i][j - 1])

	# Fill in Bottom/Right
	for i in range(len(tree_heights) - 2, -1, -1):
		for j in range(len(tree_heights[i]) -2, -1, -1):
			max_heights[i][j][BOTTOM] = max(max_heights[i + 1][j][BOTTOM], tree_heights[i + 1][j])
			max_heights[i][j][RIGHT] = max(max_heights[i][j + 1][RIGHT], tree_heights[i][j + 1])

	# Count 'em' - could do this "as we go" but this is more convenient at no algorithmic complexity cost
	count = 0
	visibility = []
	for i in range(len(tree_heights)):
		row = []
		for j in range(len(tree_heights[i])):
			for direction in range(4):
				visible = False
				if tree_heights[i][j] > max_heights[i][j][direction]:
					visible = True
					break
			if visible:
				count += 1
				row.append(tree_heights[i][j])
			else:
				row.append('x')
		visibility.append(row)
	# pprint.pprint(visibility)
	print(count)

	# Part 2 - brute force -nothing clever here. Not even going to take the "easy" optimization
	# of ignoring the edges since they are 0 (at least one edge must be zero and the product including zero iz zero)
	scores = []
	for i in range(len(tree_heights)):
		row_scores = []
		DIRECTIONS = [
			(-1, 0),
			(0, -1),
			(1, 0),
			(0, 1),
		]
		for j in range(len(tree_heights[i])):
			cardinal_scores = []

			#print(f"({i}, {j})")
			for direction in range(4):
				curr_height = tree_heights[i][j]
				count = 0
				new_i, new_j = i, j
				while True:
					di, dj = DIRECTIONS[direction]
					new_i += di 
					new_j += dj
					if 0 <= new_i < len(tree_heights) and \
					   0 <= new_j < len(tree_heights[i]):
						#print(f" -- ({new_i}, {new_j})")
						count += 1
						new_height = tree_heights[new_i][new_j]
						if new_height >= curr_height:
							break
					else:
						break
				cardinal_scores.append(count)
			row_scores.append(cardinal_scores)
		scores.append(row_scores)
	#pprint.pprint(scores)
	max_score = 0
	for score_row in scores:
		for score_column in score_row:
			product = prod(score_column)
			#print(product, end=" ")
			max_score = max(max_score, product)
		#print("")
	print(max_score)