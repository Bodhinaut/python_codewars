def solve(a, b):
	song_heaviness_Alice = a[0]
	origin_Alice = a[1]
	outfits_Alice = a[2]
	song_heaviness_Bob = b[0]
	origin_Bob = b[1]
	outfits_Bob = b[2]
	alice_score = 0
	bob_score = 0

	if song_heaviness_Alice > song_heaviness_Bob:
		alice_score += 1
	elif song_heaviness_Bob > song_heaviness_Alice:
		bob_score += 1
	else:
		alice_score = alice_score
		bob_score = bob_score

	if origin_Alice > origin_Bob:
		alice_score += 1
	elif origin_Bob > origin_Alice:
		bob_score += 1
	else:
		alice_score = alice_score
		bob_score = bob_score

	if outfits_Alice > outfits_Bob:
		alice_score += 1
	elif outfits_Bob > outfits_Alice:
		bob_score += 1
	else:
		alice_score = alice_score
		bob_score = bob_score


	if alice_score > bob_score:
		return(str(alice_score) + ", " + str(bob_score) + ': Alice made "Kurt" proud!')
	elif bob_score > alice_score:
		return(str(alice_score) + ", " + str(bob_score) + ': Bob made "Jeff" proud!')
	else:
		return(str(alice_score) + ", " + str(bob_score) + ': that looks like a "draw"! Rock on!')


solve([47, 7, 2], [47, 7, 2])





'''
def solve(a, b):    
    result_a, result_b = 0, 0     
    for i in range(len(a)):
        if a[i] > b[i]:
            result_a += 1
        elif a[i] < b[i]:
            result_b += 1
            
    if result_a > result_b:
        return '{}, {}: Alice made "Kurt" proud!'.format(result_a, result_b)
    elif result_a < result_b:
        return '{}, {}: Bob made "Jeff" proud!'.format(result_a, result_b)
    else:
        return '{}, {}: that looks like a "draw"! Rock on!'.format(result_a, result_b)

'''

# Above is another way to solve this challenge