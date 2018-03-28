def lengthofLongestSubstring(s):
    my_map = {}
    max_len = start = 0
    for i in range(len(s)):
        if s[i] not in my_map or my_map[s[i]] < start:
            max_len = max(max_len,i-start+1)
        else:
            start = my_map[s[i]]+1
        my_map[s[i]] = i
    return max_len
