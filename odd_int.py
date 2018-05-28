def find_it(seq):
	sorted_seq = sorted(seq)
	for value in seq:
		if (seq.count(value) % 3 == 0 ):
			print(value)
			break

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])




'''
def find_it(seq):
	for value in range(0, len(seq) ):
		count = 0
		for x in range(0, len(seq) ):
			if seq[value] == seq[x]:
				count += 1

		if (count % 2 != 0):
			return seq[value]

	return -1
'''

# The above is simply another way of completing this challenge, so is the below 


'''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


'''