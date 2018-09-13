def solution(digits):
    if not len(digits):
        return []
    dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    result = [""]
    for digit in digits:
        lst = dict[digit]
        newresult = []
        for char in lst:
            for str in result:
                newresult.append(str + char)
        result = newresult
    return result
h = "23"
print(solution(h))