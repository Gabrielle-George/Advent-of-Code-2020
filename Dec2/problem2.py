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
	okay_index = int(rule.split("-")[0]) - 1
	buf = rule.split("-")[1]
	bad_index = int(''.join([i for i in buf if i.isdigit()]))-1
	char = ''.join([i for i in buf if not i.isdigit()])
	#print("{} is char_min\n{} is charmax\n{}ischar".format(char_min,char_max, char))

	if ((password[okay_index]==char and password[bad_index] != char) or (password[okay_index]!=char and password[bad_index] == char)):


		counter= counter+1

print("{} is counter".format(counter))
