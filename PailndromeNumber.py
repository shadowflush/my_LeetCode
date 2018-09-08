import math
def isPalindrome(x):
    if x < 0 :
        return False
    rtype = True
    original = x
    reverse = 0
    if x == 0:
        return rtype
    digits = math.floor(math.log(x, 10))
    while x > 0:
        x, remainder = divmod(x, 10)
        reverse += remainder*pow(10,digits)
        digits -= 1
    if reverse != original:
        rtype = False
    return rtype








a = 1002001
print(isPalindrome(a))