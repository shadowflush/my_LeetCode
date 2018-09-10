def maxArea(height):
    start, end = 0, len(height)-1
    area = 0
    while start < end:
        area = max(area,(end-start)*min(height[start], height[end]))
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return area


h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))