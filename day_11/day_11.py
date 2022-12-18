import pprint
import sys

# For Part 1
# divisible = True
# rounds = 20

# For part 2
# Brute force is slow because the modulus gets slow on arbitrarily large numbers. Python can handle it, but
# it will take linear time in the number of digits which grows pretty quickly with some monkey's.
# A trivial optimization is that the final test is moduulus a number (uqique to each monkey). Since all
# operations are linear, (add or multiply) we can modulus with the LCM.. or if we're lazy (and it doesn't really matter
# for relatively few monkeys) just multiply all the divide values together and use that
DIVISIBILE = False
ROUNDS = 10000
MODULUS = 1

with open('input.txt') as input_file:
	monkeys = {}
	for i, line in enumerate(input_file):
		if i % 7 == 0:
			a,b = line.split(' ')
			monkey = int(b[::-2].strip())
			if not monkey in monkeys:
				monkeys[monkey] = {'inspects' : 0}
		elif i % 7 == 1:
			a = line.split(':')[-1]
			starting_items = list(map(lambda x: int(x.strip()), a.split(',')))
			monkeys[monkey]['items'] = starting_items
		elif i % 7 == 2:
			expr = line.split('=')[-1].strip()
			monkeys[monkey]['operation'] = expr

		elif i % 7 == 3:
			a, b = line.split(':')
			monkeys[monkey]['divisible'] = int(b.split(' ')[-1].strip())
			MODULUS *= monkeys[monkey]['divisible']
		elif i % 7 == 4:
			monkeys[monkey]['targets'] = [int(line.split(' ')[-1].strip())]
		elif i % 7 == 5:
			monkeys[monkey]['targets'].append(int(line.split(' ')[-1].strip()))

print(monkeys)

for _ in range(ROUNDS):
	#print(monkey, items, operation, divisible, targets)
	for monkey in monkeys:
		#print(f"Monkey {monkey}:")

		for item in monkeys[monkey]['items']:
			#print(f"  Monkey inspects an item with worry level of {item}.")
			monkeys[monkey]['inspects'] += 1
			old = item
			item = eval(monkeys[monkey]['operation'])
			#print(f"  Worry level is updated to {item}")
			if DIVISIBILE:
				item //= 3
			else:
				# Part 2 see optimzation
				item %= MODULUS
			#print(f"  Monkey gets bored with item. Worry level is divided by 3 to {item}.")
			tested = (item % monkeys[monkey]['divisible']) == 0
			#print(f"  Current worry level is {'' if tested else 'not '}divisible by {monkeys[monkey]['divisible']}.")
			target = monkeys[monkey]['targets'][int(not tested)]
			#print(f"Item with worry level {item} is thrown to monkey {target}")
			monkeys[target]['items'].append(item)
		monkeys[monkey]['items'] = []
	#print(monkeys)
descending = sorted(map(lambda x: (x, monkeys[x]['inspects']), monkeys), key=lambda x: -x[1])
print(descending[0][1] * descending[1][1])