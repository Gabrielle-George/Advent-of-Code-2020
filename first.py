filename = "input.txt"
file = open(filename)
nums = []

line = file.readline()

while line:
	nums.append(line)
	line = file.readline()

for i in range(len(nums)):
	for j in range(len(nums)):
		if( i + j == 2020):
			print("{} is one, {} is another.".format(i,j))
			print(i*j)