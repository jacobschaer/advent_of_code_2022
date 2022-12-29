with open('input.txt') as input_file:
	rocks = set()
	for line in input_file:
		paths = line.strip().split(' -> ')
		for i in range(len(paths) - 1):
			start, finish = paths[i], paths[i+1]
			start_x, start_y = map(int, start.split(','))
			end_x, end_y = map(int, finish.split(','))

			x = start_x
			y = start_y
			rocks.add((x,y))
			while (x != end_x) or (y != end_y):
				if end_x > x:
					x += 1
				elif end_x < x:
					x -= 1
				if end_y > y:
					y += 1
				elif end_y < y:
					y -= 1
				rocks.add((x,y))
	import pprint
	pprint.pprint(rocks)

max_y = max(map(lambda x: x[1], rocks))
print(max_y)

# Part 1
broke_through = False
sand = set()
while not broke_through:
	grain_x, grain_y = (500, 0)
	while True:
		if grain_y > max_y:
			broke_through = True
			break
		if (grain_x, grain_y + 1) not in rocks and (grain_x, grain_y + 1) not in sand:
			grain_y += 1
		elif (grain_x - 1, grain_y + 1) not in rocks and (grain_x - 1, grain_y + 1) not in sand:
			grain_x -= 1
			grain_y += 1
		elif (grain_x + 1, grain_y + 1) not in rocks and (grain_x + 1, grain_y + 1) not in sand:
			grain_x += 1
			grain_y += 1
		else:
			sand.add((grain_x, grain_y))
			break
print(len(sand))

# Part 2
sand = set()
while (500,0) not in sand:
	grain_x, grain_y = (500, 0)
	moved = True
	while moved:
		moved = False
		for candidate_position in ((grain_x, grain_y + 1), (grain_x - 1, grain_y + 1), (grain_x + 1, grain_y + 1)):
			if candidate_position not in rocks and candidate_position not in sand and candidate_position[1] < max_y + 2:
				grain_x, grain_y = candidate_position[0], candidate_position[1]
				moved = True
				break
	sand.add((grain_x, grain_y))
print(sand)
print(len(sand))
