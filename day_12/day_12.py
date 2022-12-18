import pprint
import sys

# maximum laziness
sys.setrecursionlimit(10**6)

graph = []
start = None
end = None
with open('input.txt') as input_file:
	for line in input_file:
		graph.append(list(line.strip()))

for i in range(len(graph)):
	for j in range(len(graph[i])):
		if graph[i][j] == 'S':
			start = (i,j)
		elif graph[i][j] == 'E':
			end = (i,j)

best = [[None for _ in range(len(graph[0]))] for _ in range(len(graph))]
pprint.pprint(graph)
pprint.pprint(best)
#print(start, end)

def walk(best, grid, start, distance):
	i, j = start
	#print(f"Start: {start}")
	if best[i][j] is None or distance < best[i][j]:
		best[i][j] = distance
		# We could optimize by taking the choice that gets us closest first
		# as it's mostly likely unproductive to move away most of the time,
		# but in the scheme of things it won't make much difference
		for step_i, step_j in ((0,1), (1,0), (-1, 0), (0, -1)):
			#print(f"Stepping: {step_i}, {step_j}")
			new_i, new_j = i + step_i, j + step_j
			if 0 <= new_i < len(grid) and \
				0 <= new_j < len(grid[new_i]):
				target_height = ord(grid[new_i][new_j])
				current_height = ord(grid[i][j])
				if grid[new_i][new_j] == 'E':
					target_height = ord('z')
				elif grid[i][j] == 'S':
					current_height = ord('a')
				d_height = target_height - current_height
					#print(grid[i][j], grid[new_i][new_j], d_height)
				if d_height <= 1:
					#print((i,j), (new_i, new_j), d_height)
					walk(best, grid, (new_i, new_j), distance + 1)

# Part 1
walk(best, graph, start, 0)
print(best[end[0]][end[1]])

# Part 2 - This is brute force, but it doesn't take long
# The optimal algorithm is:
# Initialize best to the value determined in part 1, as we're
# not interested in any paths to cells that are "worse" than
# the one we found. Then, start at the endpoint and work our way
# backwards using the same rules to find the best distance from 
# *any* cell.  This will save a lot of redundant routes
best_start = start
best_length = best[end[0]][end[1]]
for i in range(len(graph)):
	for j in range(len(graph[i])):
		if graph[i][j] == 'a':
			print(f"Considering ({i}, {j})")
			best = [[None for _ in range(len(graph[0]))] for _ in range(len(graph))]
			walk(best, graph, (i, j), 0)
			steps = best[end[0]][end[1]]
			#print(f"Steps: {steps}")
			if steps is not None and steps < best_length:
				best_start = (i, j)
				best_length = steps
				print(best_start, best_length)
print("*******")
print(best_start, best_length)