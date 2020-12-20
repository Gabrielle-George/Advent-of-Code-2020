filename = "input.txt"
file = open(filename)
nums = []

line = file.readline()

while line:
	nums.append(line)
	line = file.readline()

for i in nums:
	for j in nums:
		for k in nums:
			if( int(i) + int(j) +int(k)== 2020):
				print("{} is one, {} is another, {} is another.".format(int(i),int(j), int(k)))
				print(int(i)*int(j)*int(k))