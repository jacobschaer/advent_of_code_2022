import pprint
# Part 1
with open('input.txt') as input_file:
	value = 1
	current = None
	on_deck = None
	time = 1
	total = 0

	while True:
		current = on_deck
		on_deck = None

		if current is None:
			line =  input_file.readline()
			if line != '':
				print(line)
				try:
					command, command_value = line.strip().split(' ')
					if command == 'addx':
						on_deck = (command, command_value)
				except ValueError:
					current = (line.strip(), None)
			else:
				break

		if time == 20 or (time - 20) % 40 == 0:
			total += time * value
			print(f"During the {time} cycle, value is {value}")

		if current is not None:
			command, command_value = current
			if command == 'addx':
				value += int(command_value)

		#print(f"After the {time} cycle, value is {value}")
		time += 1

	print(total)

# Part 2
with open('input.txt') as input_file:
	value = 1
	current = None
	on_deck = None
	time = 1
	total = 0

	while True:
		current = on_deck
		on_deck = None

		if current is None:
			line =  input_file.readline()
			if line != '':
				try:
					command, command_value = line.strip().split(' ')
					if command == 'addx':
						on_deck = (command, command_value)
				except ValueError:
					current = (line.strip(), None)
			else:
				break

		row, column = (time - 1) // 40, (time - 1) % 40
		#print(f"CRT Draws pixel in position {column}")
		#print(f"Sprint position {value}")
		to_print = '.'
		if max(value -1, 0) <= column <= min(value + 1, 39): 
			to_print = '#'
		if column == 39:
			print(f'{to_print}')
		else:
			print(f'{to_print}', end='')


		if current is not None:
			command, command_value = current
			if command == 'addx':
				value += int(command_value)

		#print(f"After the {time} cycle, value is {value}")
		time += 1

	print(total)