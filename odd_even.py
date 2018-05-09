def oddOrEven(arr):
    sum = 0
    for x in arr:
        sum += x
    if sum % 2 == 0:
        print ("even")
        return "even"
    else:
        print ("odd")
        return "odd"


oddOrEven([0,1,2])
