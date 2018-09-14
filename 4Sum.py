def solution(nums, target):
    def Nsum(nums, target, N, result, results):  # 源数组，目标结果, 加数个数。。。。
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  #####此句可提升一个数量级的效率
            return
        if N == 2:
            start, end = 0, len(nums) - 1
            while start < end:
                sum = nums[start] + nums[end]
                if sum == target:
                    results.append(result + [nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start - 1] == nums[start]:
                        start += 1
                elif sum < target:
                    start += 1
                else:
                    end -= 1
        else:
            length = len(nums)
            for i in range(length - N + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    Nsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)
    results = []
    Nsum(sorted(nums), target, 4, [], results)
    return results
h = [-1,-5,-5,-3,2,5,0,4]
print(solution(h,-7))