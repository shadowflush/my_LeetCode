def longestCommonPrefix(strs):
    prefix = ""
    if len(strs)>0:
        strs = sorted(strs)
        length = min(len(strs[0]), len(strs[-1]))
        for i in range(length):
            if strs[0][i]==strs[-1][i]:
                prefix+=strs[0][i]
            else:
                break
    return prefix

h = ["dog","racecar","car"]
print(longestCommonPrefix(h))