def positive_sum(arr):
    pos_sum = 0
    index = 0
    while index < len(arr):
        if arr[index] > 0:
           pos_sum += arr[index]
        index += 1
    
    return(pos_sum)    




positive_sum([1, -4, 7, 12])
