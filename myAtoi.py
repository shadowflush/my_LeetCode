def myAtoi(str):
    length = len(str)
    rInt = 0
    firstIsPorD = -1 # 0 represent - ; 1 represent +
    calculate = False
    str = str.lstrip()
    length = len(str)
    if length == 0:
        return 0l
    if str[0] == '+':
        firstIsPorD = 1
    elif str[0] == '-':
        firstIsPorD = 0
    elif ord(str[0]) >= 48 and ord(str[0]) <= 57:
        rInt+=ord(str[0])-48
        calculate = True
    else:
        return 0
    for i in range(1,length):
        tmp = ord(str[i])
        if tmp<48 or tmp>57:
            break
        rInt = rInt*10 + tmp - 48
    rInt = -rInt if firstIsPorD==0 else rInt
    if firstIsPorD==0:
        rInt = -pow(2,31) if rInt < -pow(2,31) else rInt
    else:
        rInt = pow(2,31)-1 if rInt > pow(2,31) -1 else rInt
    return rInt





a = " ww 123"
print(myAtoi(a))