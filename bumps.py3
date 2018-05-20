def bumps(road):
	bump_count = 0
	road_array = list(road)
	for bumps in road_array:
		if bumps == 'n':
			bump_count += 1
	if bump_count > 15:
		return("Car Dead")
	else:
		return("Woohoo!")
# test case below
bumps("nn_nnnn__nn___n____n___nn__nnn")