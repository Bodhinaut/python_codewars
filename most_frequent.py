def most_frequent_item_count(collection):
	if collection:
		return max([collection.count(item) for item in collection])
	return 0



most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])