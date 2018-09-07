def convert(s,numRows):
    reS = ""
    if numRows == 1:
        return s
    for i in range(numRows):
        if i == 0 or i == numRows - 1:
            reS = reS + "".join(s[i::2*numRows-2])
        else:
            index = i
            while index < len(s):
                reS = reS + s[index]
                if (index+(numRows-1-i)*2) < len(s):
                    reS += s[index+(numRows-1-i)*2]
                index += 2*numRows-2
    return reS



a = "PAYPALISHIRING"
print(convert(a,4))