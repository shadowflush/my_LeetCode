def my_leetcode(s):
     length = len(s)
     half_max_length = 0
     startIndex = endIndex = 0
     for i in range(0,length):
         half_length = 0
         while i-half_length>0 and i+half_length<length-1 and s[i-half_length-1]==s[i+half_length+1]:
             half_length+=1
             if half_length>=half_max_length:
                 half_max_length = half_length
                 startIndex = i- half_length
                 endIndex = i +half_length
         half_length = 0
         while i - half_length>=0 and i+half_length<length-1 and s[i-half_length]==s[i+half_length+1]:
             half_length +=1
             if half_length >half_max_length:
                 half_max_length = half_length
                 startIndex = i-half_length+1
                 endIndex = i+half_length
     return s[startIndex:endIndex+1]

a = "aaabaaaa"
print(my_leetcode(a))