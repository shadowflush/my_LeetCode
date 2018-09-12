def solution(nums):
    nums.sort()
    length = len(nums)
    reList = []
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        start, end = i + 1, length - 1
        num1 = nums[i]
        if num1 > 0:
            break
        while start < end:
            num2, num3 = nums[start], nums[end]
            if num1 + num2 + num3 < 0:
                start += 1
            elif num1 + num2 + num3 > 0:
                end -= 1
            else:
                reList.append([num1, num2, num3])
                start += 1
                end -= 1
                while nums[start - 1] == nums[start] and start < end:
                    start += 1
    return reList
h = [-1,0,1,2,-1,-4]
print(solution(h))