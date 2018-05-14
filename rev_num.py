def reverseNumber(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return int(str(n).strip('-')[::-1])*-1

reverseNumber(-123)
