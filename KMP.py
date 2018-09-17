def solution(haystack, needle):
    def buildNext(needle):
        length = len(needle)
        next = [0] * length
        i, j, next[0] = -1, 0, -1
        while j < length - 1:
            if i < 0 or needle[j] == needle[i]:
                i += 1
                j += 1
                next[j] = next[i] if needle[j] == needle[i] else i
                j += 1
            else:
                i = next[i]
        return next

    lengthH, lengthN = len(haystack), len(needle)
    if lengthN == 0:
        return -1
    next = buildNext(needle)
    i, j = 0, 0
    while i < lengthH and j < lengthN:
        if j < 0 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    return i - j




s = "a"
print(solution("ababcaababcaabc","ababcaabc"))