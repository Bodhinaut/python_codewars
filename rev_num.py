def reverse_number(n):
    boolNeg = False
    if n < 0:
        boolNeg = True
    stringN = str(n)
    list(stringN)
    if stringN[0] == "-":
        stringN = stringN[1:]
    stringN = stringN[::-1]
    stringN = int(stringN)
    if boolNeg == True:
        stringN *= -1
    print(stringN)
    return stringN

reverse_number(-123)
