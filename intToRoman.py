def intToRoman(num):
    roman = ""
    divisors = [1000, 500, 100, 50, 10, 5, 1, 0, 0]
    code = ['M','D','C','L','X','V','I']
    i = 0
    while i < 7:
        quotient, num = divmod(num, divisors[i])
        roman += code[i]*quotient
        if not i%2 and num+divisors[i+2]>=divisors[i]:
            roman+=code[i+2]+code[i]
            num -= divisors[i] - divisors[i+2]
        elif i%2 and num+divisors[i+1]>=divisors[i]:
            roman+=code[i+1]+code[i]
            num-= divisors[i] - divisors[i+1]
        i+=1
    return roman


h = 1994
print(intToRoman(h))