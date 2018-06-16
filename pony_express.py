# def riders(stations):
# 	max_miles = 0
# 	riders = 1

# 	if sum(stations) < 100:
# 		return (1)
# 	else:
# 		for miles in stations:
# 			max_miles += miles
# 			if max_miles > 99:
# 				max_miles = miles
# 				riders += 1

# 	return(riders)


# def riders(stations):
# 	max_miles = sum(stations)
# 	riders_miles = 0
# 	riders = 0
# 	if max_miles < 100:
# 		riders += 1
# 	else:
# 		while riders_miles <= max_miles:
# 			riders_miles += 100
# 			#max_miles -= 100
# 			print(max_miles)
# 			print(riders_miles)
# 			riders += 1
# 	return(riders)


# def riders(stations):
# 	current_miles = 0
# 	riders = 1
# 	if sum(stations) < 100:
# 		return (riders)
# 	else:
# 		for miles in stations:
# 			temp = 0
# 			if temp > 0:
# 				current_miles += temp
# 				temp = 0
# 			current_miles += miles
# 			if current_miles > 100:
# 				riders += 1
# 				temp = current_miles - 100
# 				current_miles = 0
# 		return (riders)


def riders(stations):
	current_miles = 0
	riders = 1
	if sum(stations) <= 100:
		return(riders)
	else:
		index = 0
		while index < len(stations):
			current_miles += stations[index] 
			if current_miles > 100:
				riders += 1
				current_miles = stations[index]

			index += 1
	return (riders)


print(riders([36, 8, 32, 45]) ) # should return 2