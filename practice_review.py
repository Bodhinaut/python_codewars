
def array_diff(a, b):
	b = set(b)
	print ([c for c in a if c not in b])


array_diff([1,2,2], [1])


import math

def get_average(marks):
	print(math.floor( sum(marks) / len(marks) ) )

get_average([2,5,13,25,13,45,16,5,12,2])


def bumps(road):
	print ("Woohoo!") if road.count("n") <= 15 else print ("Car Dead")

bumps("nn_nnnn__nn___n____n___nn__nnnnnnnnnnnnn")


def gimme(array):
	print ( array.index(sorted(array)[1]) )

gimme([2,3,1])


def frequent(list):
	if list:
		print ( max([list.count(value) for value in list]) )
	else:
		print (0)

frequent([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])


def accum(s):
	output = ""
	for i in range(len(s) ):
		output += (s[i] * (i + 1) ) + "-"
	print (output.title()[:-1])

accum("abcd")


def powers_of_two(n):
	times_2 = [2 ** value for value in range(0, n + 1)]
	print(times_2)

powers_of_two(5)


def reverse_number(n):
	if n >= 0:
		print(int(str(n)[::-1]))
	else:
		print(int(str(n).strip('-')[::-1]) * -1)

reverse_number(-123)


def rev_seq(n):
	print (list(range(n, 0, -1)))

rev_seq(5)


def two_sort(a):
	a = sorted(a)
	result = a[0]
	result = result.replace("", "***")
	print (result[3:-3])

two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])


