def median(nums1, nums2):
    len1, len2 = len(nums1), len(nums2)
    if len1 > len2:#make sure len(nums1)<=len(nums2)
        nums1,nums2,len1,len2 = nums2,nums1,len2,len1
    if len1 == 0:# if one list is empty
        if len2%2:
            return nums2[len2//2]
        else:
            return (nums2[len2//2]+nums2[len2//2-1])/2

    i_former, i_later, half_len = 0, len1, (len1 + len2 + 1) // 2
    while i_former <= i_later:
        i = (i_former + i_later) // 2
        j = half_len - i
        if i < len1 and nums2[j-1] > nums1[i]:#L2>R1,i < we want
            i_former = i + 1
        elif i >0 and nums1[i-1] > nums2[j]:#L1>R2, i > we want
            i_later = i - 1
        else:# i is we want
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else:max_of_left = max(nums1[i-1], nums2[j-1])

            if i == len1: min_of_right = nums2[j]
            elif j == len2: min_of_right = nums1[i]
            else:min_of_right = min(nums1[i],nums[j])


            if (len1+len2)%2:# if len1+len2 is odd max_of_left is we want. in order to cut down runtime ,place this statement at here not the end
                return max_of_left
            else:
                return (max_of_left + min_of_right) / 2.0

a = [7]
c = [6,7,8,9]
d=median(a,c)
print(d)