import math
def get_average(marks):
    sum = 0
    for grades in marks:
    	sum += grades

    print( math.floor(sum / len(marks) ) )





get_average([2,5,13,20,16,16,10])