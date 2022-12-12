count = 0
with open('input.txt') as input_file:
	for line in input_file:
		elf_ranges = []
		for elf_range in line.split(','):
			elf_ranges.append(list(map(int, elf_range.split('-'))))

		a, b, c, d = elf_ranges[0][0], elf_ranges[0][1], elf_ranges[1][0], elf_ranges[1][1]

		if c <= a and b <= d:
			# left fully contained within right
			count += 1
		elif c >= a and d <= b:
			# right fully contained within left
			count += 1

print(count)


count = 0
with open('input.txt') as input_file:
	for line in input_file:
		elf_ranges = []
		for elf_range in line.split(','):
			elf_ranges.append(list(map(int, elf_range.split('-'))))

		elf_ranges.sort()
		a, b, c, d = elf_ranges[0][0], elf_ranges[0][1], elf_ranges[1][0], elf_ranges[1][1]

		if c <= b:
			count += 1
print(count)
