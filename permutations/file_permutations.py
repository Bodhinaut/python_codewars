def open_file(filename):
	"""
	Reads in each line of a file and stores into an array
	"""
	with open(filename) as file_object:
		lines = file_object.readlines()

	array = []

	for line in lines:
		array.append(line.rstrip() ) # removes new line '\n'

	return(array) # return array of strings to be permutated

# insert string of file to be read in, the returned array is then set to be permute variable
permute = open_file('sample_input.txt') 
# --------------------------------------

def permutations(permute):
	if len(permute) == 1: return set(permute)
	first = permute[0]
	following = permutations(permute[1:] )
	result = set()
	for value in range(0, len(permute) ):
		for values in following:
			result.add(values[0:value] + first + values[value:] )
	return(result)


index = 0
while index < len(permute):
	print(sorted(permutations(permute[index]) ) )
	index += 1
