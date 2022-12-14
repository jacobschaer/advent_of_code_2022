with open('input.txt') as input_file:
	size = 14
	fifo = []
	for i, character in enumerate(input_file.read()):
		if len(fifo) < size:
			fifo.append(character)
		else:
			if len(set(fifo)) == size:
				print(i)
				break
			fifo.pop(0)
			fifo.append(character)