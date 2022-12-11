
# Part 1
total = 0
with open('input.txt') as input_file:
	for line in input_file:
		priorities = []
		num_priorities = 0
		for char in line.strip():
			offset = 27
			index = 'A'
			if char.islower():
				index = 'a'
				offset = 1
			priorities.append(ord(char) - ord(index) + offset)
			num_priorities += 1

		comp1, comp2 = priorities[0:num_priorities // 2], priorities[num_priorities // 2:]
		intersection = set(comp1) & set(comp2)
		total += sum(intersection)
	print(total)

# Part 2
with open('input.txt') as input_file:
	group = []
	total = 0
	for line in input_file:
		priorities = []
		num_priorities = 0
		for char in line.strip():
			offset = 27
			index = 'A'
			if char.islower():
				index = 'a'
				offset = 1
			priorities.append(ord(char) - ord(index) + offset)
			num_priorities += 1
		group.append(priorities)
		if len(group) == 3:
			intersection = set(group[0])
			intersection &= set(group[1])
			intersection &= set(group[2])
			total += sum(intersection)
			group = []
	print(total)