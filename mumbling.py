def accum(s):
	answer = ""
	stored_string = []
	string = [value.upper() for value in list(s)]
	# print(string)
	index = 0
	while index < len(s):
		# print (string[index])
		if index == 0:
			stored_string.append(string[index] + "-")
		elif index == (len(s) -1):
			temp = (string[index].lower() * index)
			stored_string.append(string[index] + temp)
		else:
			temp = (string[index].lower() * index)
			stored_string.append(string[index] + temp + "-" )
		index += 1

	for value in stored_string:
		answer += value

	return (answer)


accum("abcd")