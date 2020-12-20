import re

def byr(value):
	return (len(value)==4) and (int(value)>=1920) and (int(value)<=2002)

def iyr(value):
	return (len(value)==4) and (int(value)>=2010) and (int(value)<=2020)

def eyr(value):
	return (len(value)==4) and (int(value)>=2010) and (int(value)<=2030)

def hgt(value):
	cm = value[-2:] == "cm"
	inch = value[-2:] == "in"
	value = ''.join(c for c in value if c.isdigit())
	cm = cm and ((int(value) >= 150) and (int(value) <= 193))
	inch = inch and ((int(value) >= 59) and (int(value) <= 76))
	return (cm or inch)

def hcl(value):
	hashtag = value[0] =="#"
	value = value.replace("#","")
	length = len(value)==6
	valid = bool(re.match('^[a-z0-9]+$', value))
	return valid and hashtag and length

def ecl(value):
	return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(value):
	valid = bool(re.match('^[0-9]+$', value))
	length = len(value)==9
	return valid and length

validation_functions = {"byr":byr, "iyr":iyr, "eyr":eyr, "hgt":hgt, "hcl":hcl, "ecl":ecl, "pid":pid}

def validate(field):
	return validation_functions[field[0]](field[1])




filename = "input.txt"
file = open(filename)
passport = file.read()

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
valid = []
items = {}
for j in passports:

	temp = j.split()
	if ((len(temp) ==8) or (len(temp)==7 and not("cid" in j))):
		valid.append(dict(i.split(":") for i in temp))

for i in valid:
	is_valid = True
	i.pop("cid", None)
	for key in i.keys():
		is_valid = validation_functions[key](i[key]) and is_valid #if any is false then the answer becomes false
	counter = counter+is_valid

print(counter)

















