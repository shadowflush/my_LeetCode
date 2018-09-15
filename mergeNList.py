class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def solution(lists):
    def mergeTwo(l1, l2,re):
        length1,length2 = len(l1),len(l2)
        right = ListNode(0)
        left = ListNode(0)
        if length1 == 0 and length2 == 1:
            re.next = l2[0]
            return
        if length1 > 0 :
            mergeTwo(l1[:length1//2],l1[length1//2:],right)
        if length2 > 0:
            mergeTwo(l2[:length2//2],l2[length2//2:],left)
        headL1, headL2, headL3 = right.next, left.next, re
        while headL1 and headL2:
            if headL1.val < headL2.val:
                headL3.next = ListNode(headL1.val)
                headL1 = headL1.next
            else:
                headL3.next = ListNode(headL2.val)
                headL2 = headL2.next
            headL3 = headL3.next
        if headL1:
            headL3.next = headL1
        else:
            headL3.next = headL2

    length = len(lists)
    re = ListNode(0)
    mergeTwo(lists[:length//2],lists[length//2:],re)
    return re.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(3)
l3.next = ListNode(4)
l3.next.next = ListNode(4)

l4 = ListNode(1)
l4.next = ListNode(5)
l4.next.next = ListNode(6)

lists = [l1,l2,l3,l4]
solution(lists)
print('fff')