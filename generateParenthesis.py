def solution(n):
    def results(right, rightCount, left, str, list):
        if right != 0:
            results(right - 1,rightCount + 1, left, str+'(', list)
        if left != 0 and rightCount != 0:
            results(right,rightCount - 1, left - 1, str+')', list)
        if left == 0 and right == 0:
            list.append(str)
    list = []
    results(n,0,n,"",list)
    return list

print(solution(3))