'''
def sort_by_length(arr):
    newlist = []
    newlist.append(arr[0])
    for i in arr[1:]:
        for x in range(len(newlist)):
            if len(i) < len(newlist[0]):
                newlist.insert(0,i)
                break
            elif len(i) < len(newlist[x]):
                newlist.insert(x,i)
                break
            elif len(i) > len(newlist[-1]):
                newlist.append(i)
                break
    return newlist
'''


def sort_by_length(arr):
    return sorted(arr, key=len)

sort_by_length(["beg", "life", "i", "to"])