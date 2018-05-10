"""
def two_sort(array):
    answ = ""
    array.sort()
    first_val = array[0]
    first_val = list(first_val)
    for x in first_val:
        if x != first_val[-1]:
            answ += (x + '***')
        else:
            answ += x
    return(answ)
"""

def two_sort(a):
    a = sorted(a)
    result = a[0]
    result = result.replace("", "***")
    return result [3:-3]



two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])

