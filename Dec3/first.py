import numpy as np
filename = "input.txt"
file = open(filename)

line = file.readline()
forest = []

while line:
	forest.append(line.replace("\n",""))
	line = file.readline()


counter = 0

#the lengths of the strings are 31 characters


#forest = ["....#..#....#","..##.#.#.#...",".........#.#.",".....##.....#","....#..#....#","..##.#.#.#...",".........#.#.",".....##.....#"]
x = 0
y = 0
mod_val = len(forest[0])

while (y <len(forest)):
	if (forest[y][x] == "#"):
		counter = counter+1
	x = (x+1)%mod_val
	y = y+2

print(counter)
print(37*47*64*61*257)