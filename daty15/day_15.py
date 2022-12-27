#-*-coding:utf8;-*-
#qpy:console

import pathlib
import os
import re

base_path = pathlib.Path().absolute()


#print("This is console module")
print(base_path)
print(__file__)

with open(os.path.join(base_path, "projects3/Test/input.txt")) as myfile:
    points = []
    for line in myfile:
        match = re.match(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([0-9]+)', line)
        if not match:
            continue
        x1, y1, x2, y2 = map(int, match.groups())
        distance = abs(y2 - y1) + abs(x2 - x1)
        points.append((x1,y1, distance))
        
    for x,y,distance in points:
        print('----')
        print(x,y,distance)
        print("----")
        max_search = 4000000
        for i in range(x - (distance + 1), x + (distance + 2)):
            # distance = abs(x - i) + abs(y - j)
            # abs(y - j) = distance - abs(x - i)
            # y - j = +/-(distance - abs(x -i))
            # j = y + (distance - abs(x-i))
            # j = y - (distance - abs(x-i))
            z = (distance - abs(x - i))
            # We could be more precise, we really just want the ones that are 1 greater
            # than the distance. If there truly is exactly 1 gap, then it must appear on a
            # boundary or else there would be multiples. So, we calculate the y coordinate
            # and then try a few possibilities (above, below, on the money, etc) and then
            # check if it meets our search conditions. If it does, check each point against
            # all other sensors to see if it should have been detected
            # Finds the candidate in around 20 seconds on my android tablet
            for j in (y + z + 1, y + z, y + z -1, y - z, y - z + 1, y - z - 1):
                if 0 <= i <= max_search and 0 <= j <= max_search:
                    #print((i,j,abs(x - i) + abs(y - j)))
                    is_available = True
                    for other_x, other_y, other_distance in points:
                        if abs(other_x - i) + abs(other_y - j) <= other_distance:
                            is_available = False
                            break
                    if is_available:
                        frequency = (i * 4000000) + j
                        print(f"Winner: ({i}, {j}). Frequency: {frequency}")
                        break
