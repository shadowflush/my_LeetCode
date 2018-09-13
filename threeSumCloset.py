def solution(nums, target):
    nums.sort()
    length = len(nums)
    sum = nums[0]+nums[1]+nums[length-1]
    for i in range(length-2):
        start, end = i+1, length-1
        while start<end:
            sum1 = nums[i] + nums[start] + nums[end]
            if sum1==target:
                return sum1
            elif sum1<target:
                start+=1
            elif sum1>target:
                end-=1
            if abs(sum - target) > abs(sum1 - target):
                sum = sum1
    return sum
h = [-1, 2, 1, -4]
print(solution(h,1))