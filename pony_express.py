def riders(stations):
	riders, travelled = 1, 0

	for miles in stations:
		if travelled + miles > 100:
			riders += 1
			travelled = miles
		else:
			travelled += miles
	return(riders)

print(riders([36, 8, 32, 45]) ) # test case