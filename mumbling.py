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

	print (answer)
	# return (answer)


accum("abcd")



# below are shorter versions
'''

def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]


# --------------------------------------

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))




# end shorter versions 


'''










