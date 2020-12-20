import numpy as np
filename = "input.txt"
file = open(filename)

line = file.readline()
passport = ""

while line:
	passport = passport + line
	line = file.readline()

#can't we just count the elements and if it's one less check to see if cid is there

chunk = ""
full_chunk = ""
passports = []
for i in range(len(passport)):

	if ((passport[i] == '\n' and passport[i-1]=='\n') or i+1 >= len(passport)):
		#new chunk!
		full_chunk = chunk
		chunk = ""
	else:
		newchar = passport[i]
		if (newchar =='\n'):
			newchar = " "
		chunk = chunk + newchar

	if (full_chunk != ""):
		passports.append(full_chunk.replace("\n",""))
		full_chunk = ""

counter = 0
for j in passports:
	print(j)
	temp = j.split()
	if ((len(temp) ==8) or (len(temp)==7 and not("cid" in j))):

		counter +=1;

print(counter)