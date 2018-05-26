def sort_by_length(arr):
	short_to_long = []

	index = 0
	while index < len(arr) - 1:
		#print (len(arr[index]) )
		if len(arr[index]) > len(arr[index + 1]):
			temp = arr[index + 1]
			del arr[index + 1]
			arr.insert(index, temp)

		index += 1

	index = 0
	while index < len(arr) - 1:
		#print (len(arr[index]) )
		if len(arr[index]) > len(arr[index + 1]):
			temp = arr[index + 1]
			del arr[index + 1]
			arr.insert(index, temp)

		index += 1




	print(arr)


sort_by_length(["beg", "life", "i", "to"])