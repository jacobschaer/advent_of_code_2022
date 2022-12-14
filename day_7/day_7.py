import pprint
import re
from collections import defaultdict

def get_tree_node(root, path):
	path = path.strip()
	if path and path[0] == '/':
		path = path[1:]
	
	if path:
		components = path.split('/')
		result = root
		for component in components:
			if not component:
				break
			result = result['directories'][component]
		return result
	else:
		return root

def bfs_print(root, path=''):
	for file, size in root['files'].items():
		print('/'.join([path, file]), size)
	for directory_name, directory in root['directories'].items():
		bfs_print(directory, path='/'.join([path, directory_name]))

def bfs_sum(root, result, path=''):
	result[path] = result.get(path, 0)
	for file, size in root['files'].items():
		result[path] += size
	for directory_name, directory in root['directories'].items():
		result[path] += bfs_sum(directory, result, path='/'.join([path, directory_name]))
	return result[path]


with open('input.txt') as input_file:
	current_path = ''
	current_command = None

	root = {
	    'files' : {},
	    'directories' : {}
	}

	for line in input_file:
		#print('-------------')

		#print(f'Line: "{line.strip()}"')
		#print(f'CWD: "{current_path}"')
		#pprint.pprint(root)

		tree_node = get_tree_node(root, current_path)

		match = re.findall(r'\$ cd (.+?)$', line)

		if match:
			current_command = 'cd'
			directory = match[0].strip()
			if directory == '/':
				current_path = ''
			elif directory == '..':
				current_path = '/'.join(current_path.split('/')[:-1])
			else:
				# if not directory in tree_node['directories']:
				# 	tree_node['directories'][directory] = {
				# 	    'files' : {},
				# 	    'directories' : {}
				# 	}
				current_path = '/'.join([current_path, directory])
			continue

		if '$ ls' == line.strip():
			current_command = 'ls'
			continue

		if current_command == 'ls':
			a, b = line.split(' ')
			a, b = a.strip(), b.strip()
			if a == 'dir':
				if b not in tree_node['directories']:
					tree_node['directories'][b] = {
					    'files' : {},
					    'directories' : {}
					}
			else:
				if b not in tree_node['files']:
					tree_node['files'][b] = int(a)

	bfs_print(root)
	result = {}
	overall_total = bfs_sum(root, result)


	# Part 1
	total = 0
	for z in result:
		if result[z] <= 100000:
			total += result[z]
	print("---- Part 1: ----")
	print(total)

	# Part 2
	print("---- Part 2: ----")
	print(f"Overall total: {overall_total}")
	needs = 30000000 - (70000000 - overall_total)
	print(f"Needs: {needs}")
	to_delete = sorted(list(filter(lambda x: x[1] >= needs, result.items())), key=lambda x: x[1])[0]
	print(f"Delete: '{to_delete[0]}' at {to_delete[1]} bytes")

