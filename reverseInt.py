def reverse(x):
    lessThanZero =  1 if x >=0 else 0
    x = abs(x)
    remiander = 0
    rInt = 0
    multiple = 10
    while x > 0:
        x,remiander = divmod(x,multiple)
        rInt = rInt*multiple + remiander
    return rInt if lessThanZero else rInt*-1



a = -120
print(reverse(a))