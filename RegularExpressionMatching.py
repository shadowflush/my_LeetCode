def isMatch(s,p):
    buff = {}
    lengthS, lengthP = len(s), len(p)
    def DP(i,j):
        if (i,j) not in buff:
            if j == lengthP:#out of range means match or not match
                flag = i == lengthS
            else:
                first = i < lengthS and p[j] in {s[i], '.'}
                if j < lengthP - 1 and p[j+1] == '*':
                    flag = DP(i, j+2) or first and DP(i+1, j)
                else:
                    flag = first and DP(i+1, j+1)
            buff[i,j] = flag
        return buff[i,j]
    return(DP(0,0))





print(isMatch("aa",".*"))