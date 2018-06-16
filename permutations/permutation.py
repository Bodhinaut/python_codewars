def permutations(string):
	if len(string) == 1: return set(string)
	first = string[0]
	following = permutations(string[1:] )
	result = set()
	for value in range(0, len(string) ):
		for values in following:
			result.add(values[0:value] + first + values[value:] )
	return(result)


print(sorted(permutations('hat') ) )


