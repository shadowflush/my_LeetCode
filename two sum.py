def two_sum(nums, target):
    if len(nums) <= 1:
        return False
    my_map = {}
    for i in range(len(nums)):
        if nums[i] in my_map:
            return [my_map[nums[i]], i]
        else:
            my_map[target-nums[i]] = i
test = two_sum([15,2,7,-8,4,2], 7)
print(test)
#value + key = target