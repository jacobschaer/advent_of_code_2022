import pprint

def compare(x,y):
	#print(f"Comparing {x} v {y}")
	if type(x) == int and type(y) == int:
		return y - x
	elif type(x) == list and type(y) == list:
		i, j = 0, 0
		while True:
			if i < len(x) and j >= len(y):
				return -1
			elif i >= len(x) and j < len(y):
				return 1
			elif i >= len(x) and j >= len(y):
				return 0
			cmp_value = compare(x[i], y[j])
			if cmp_value > 0:
				return 1
			elif cmp_value < 0:
				return -1
			i += 1
			j += 1
		return -1
	elif type(x) == list:
		return compare(x, [y])
	else:
		return compare([x], y)

	# #print(f"Comparing {x} vs {y}")
	# while True:
	# 	try:
	# 		l, r = x.pop(0), y.pop(0)
	# 		if type(l) == int and type(r) == int:
	# 			if l <= r:
	# 				return True
	# 			elif r < l:
	# 				return False
	# 		else:
	# 			if type(l) == int:
	# 				l = [l]
	# 			if type(r) == int:
	# 				r = [r]
	# 			return compare(l, r)
	# 	except IndexError:
	# 		#print("Ran out")
	# 		return True

# Part 1
with open('input.txt') as input_file:
	total = 0
	packet = [[],[]]
	for i, line in enumerate(input_file):
		if i % 3 == 0:
			packet[0] = eval(line.strip())
		elif i % 3 == 1:
			packet[1] = eval(line.strip())
		else:
			#print(packet)
			cmp_value = compare(packet[0], packet[1])
			print(i // 3 + 1, cmp_value >= 0)
			if cmp_value >= 0:
				total += i // 3 + 1
	print(total)

# Part 2
import functools
with open('input.txt') as input_file:
	total = 0
	packets = [[[2]], [[6]]]
	for i, line in enumerate(input_file):
		if i % 3 == 2:
			continue
		else:
			packets.append(eval(line.strip()))

	decoder = 1
	for i, row in enumerate(sorted(packets, reverse=True, key=functools.cmp_to_key(lambda x,y: compare(x,y)))):
		print(row)
		if row in ([[2]], [[6]]):
			decoder *= i + 1
	print(decoder)
	# 		cmp_value = compare(packet[0], packet[1])
	# 		print(i // 3 + 1, cmp_value >= 0)
	# 		if cmp_value >= 0:
	# 			total += i // 3 + 1
	# print(total)