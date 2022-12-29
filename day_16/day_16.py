#-*-coding:utf8;-*-
#qpy:console

import pathlib
import os
import re
import copy
import pprint
import sys

sys.setrecursionlimit(100000)

base_path = pathlib.Path().absolute()


#print("This is console module")
print(base_path)
print(__file__)

best = 0
offset = 0

def dfs(node, graph, shortest_paths, state=None):
    global best
    if state is None:
        state = {'time': 0, 'possibilities' : set([x for x in graph if graph[x]['rate'] != 0]), 'score': 0}

    if state['time'] < 30:
        for destination in state['possibilities']:
            distance = shortest_paths[(node, destination)] + 1
            value = (30 - (state['time'] + distance)) * graph[destination]['rate']
            new_state = copy.deepcopy(state)
            new_state['time'] += distance
            new_state['score'] += value
            new_state['possibilities'].remove(destination)
            if new_state['score'] > best:
                print(new_state['score'])
                best = new_state['score']
            dfs(destination, graph, shortest_paths, new_state)
        

def shortest(graph):
    def recurse(origin, node, graph, shortest_paths, depth):
        for destination in graph[node]['leads']:
            if node != origin:
                shortest_paths[(node, destination)] = 1
                shortest_paths[(destination, node)] = 1
            if shortest_paths.get((origin, destination), 999999999) >= depth:
                shortest_paths[(origin, destination)] = depth
                shortest_paths[(destination, origin)] = depth
                recurse(origin, destination, graph, shortest_paths, depth + 1)
        
    shortest_paths = {}
    for node in graph:
        shortest_paths[(node,  node)] = 0
        recurse(node, node, graph, shortest_paths, 1)
    return shortest_paths
                    

graph = {}
with open("input.txt") as myfile:
    points = []
    for line in myfile:
        match = re.match(r'Valve ([A-Z]+) has flow rate=([0-9]+); tunnel(s?) lead(s?) to valve(s?) ([A-Z, ]+)', line)
        #if not match:
        #    continue
        valve, rate, _, _, _, leads = match.groups()
        rate = int(rate)
        leads = list(map(lambda x: x.strip(), leads.split(',')))
        graph[valve] = {'leads' : leads, 'rate' : rate}
        print(valve, rate, leads)


shortest_paths = shortest(graph)
pprint.pprint(shortest_paths)
dfs('AA', graph, shortest_paths)