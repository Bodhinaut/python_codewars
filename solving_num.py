value = []
items = [x for x in input("Please input 4 digit binary numbers seperated by commas: ").split(',')]

for p in items:
	intp = int(p, 2)
	if not intp % 5:
		value.append(p)

print (','.join(value))

