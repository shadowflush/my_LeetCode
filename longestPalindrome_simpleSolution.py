def  my_function(str1):
    str2 = str1[::-1]
    len1= len(str1)
    matrix = [[0]*(len1+1) for i in range(0,len1+1)]
    for i in range(0,len1):
        for j in range(0,len1):
            if str2[i] == str1[j]:
                matrix[i+1][j+1]=matrix[i][j]+1
            else:
                matrix[i+1][j+1]=0
    max_length = 0
    i_start = i_end = 0
    for i in range(1,len1+1):
        for j in range(1,len1+1):
            if matrix[i][j]>max_length and (len1-i==j-matrix[i][j]):
                max_length = matrix[i][j]
                i_end,i_start = j,j-max_length
    if i_end-i_start==1:
        return None
    else:
        return str1[i_start:i_end]

a = "abcfgcba"
c = my_function(a)
print(c)