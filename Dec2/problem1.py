filename = "input.txt"
file = open(filename)

#read in the lines

passwords = []

line = file.readline()

while line:
	passwords.append(line)
	line = file.readline()

#do the thing: scrape
counter = 0
for full_line in passwords:
	rule, password = full_line.replace(" ","").split(":")
	char_min = int(rule.split("-")[0])
	buf = rule.split("-")[1]
	char_max = int(''.join([i for i in buf if i.isdigit()]))
	char = ''.join([i for i in buf if not i.isdigit()])
	#print("{} is char_min\n{} is charmax\n{}ischar".format(char_min,char_max, char))

	if (password.count(char) <=char_max and password.count(char) >=char_min):
		counter= counter+1

print("{} is counter".format(counter))
