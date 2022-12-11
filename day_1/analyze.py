elves = []
with open('input') as myfile:
	elf = []
	for line in myfile:
		if line.strip():
			elf.append(int(line))
		else:
			elves.append(elf)
			#print(elf)
			elf = []
print(sum(sorted(list(map(sum, elves)))[-3:]))