def find_it(seq):
	sorted_seq = sorted(seq)
	for value in seq:
		if (seq.count(value) % 3 == 0 ):
			print(value)
			break
	#print(sorted_seq)


find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])