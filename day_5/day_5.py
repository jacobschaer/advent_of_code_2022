import re

piles = []
with open('input.txt') as input_file:
	for line in input_file:
		match = re.findall(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)', line)
		if match:
			count, pile_a, pile_b = map(int, match[0])
			# For Part A
			#for _ in range(count):
			#	piles[pile_b - 1].insert(0, piles[pile_a - 1].pop(0))
			# For Part B
			piles[pile_b - 1] = piles[pile_a - 1][0:count] + piles[pile_b -1][:]
			piles[pile_a - 1] = piles[pile_a - 1][count:]
		else:
			for match in re.finditer(r'\[([A-Z])\]', line):
				letter = match.groups(0)[0]
				column = match.span()[0] // 4
				print(column, letter)
				while len(piles) <= column:
					piles.append([])
				piles[column].append(letter)
	print(piles)
	print(''.join(map(lambda x: x[0] if x else '', piles)))