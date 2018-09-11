def romanToInt(roman):
    divisors = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    i = num = 0
    length = len(roman)
    while i < length:
        current = divisors[roman[i]]
        if i<length-1 and divisors[roman[i+1]] > current:
            num+=divisors[roman[i+1]]-current
            i+=2
        else:
            num+=current
            i+=1
    return num


h = "IV"
print(romanToInt(h))