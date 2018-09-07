def longestPalindrome(S):
    T = []
    for c in S:
        T.append('#')
        T.append(c)
    T.append('#')
    length = len(T)
    P = [0]*length
    C,R = 0,0
    maxLen = 0
    index = 0
    for i in range(length):
        i_mirror = 2*C - i
        P[i] = min((R-i),P[i_mirror]) if i<R else 0

        while (i+P[i]+1) <= length-1 and (i-P[i]-1) >= 0 and ((T[i+P[i]+1]) == (T[i-P[i]-1])):# expand
            P[i]+=1

        if (i+P[i]) > R:#change C and R
            C = i
            R = i+P[i]
        if P[i] > maxLen:
            maxLen = P[i]
            index = i
    return "".join(T[index-maxLen+1:index+maxLen+1:2])



a = "aabaacaab"
print(longestPalindrome(a))