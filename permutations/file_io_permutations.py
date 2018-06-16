filename = 'sample_input.txt'

# with open(filename) as file_object:
# 	contents = file_object.read()
# 	print(contents.rstrip() )

# with open(filename) as file_object:
# 	for line in file_object:
# 		print(line.rstrip() )

with open(filename) as file_object:
	lines = file_object.readlines()

test = []

for line in lines:
	test.append(line.rstrip() )


print(test)