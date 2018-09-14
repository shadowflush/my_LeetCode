class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def solution(l1,l2):
    result = ListNode(0)
    headL1,headL2,headL3 = l1,l2,result
    while headL1 and headL2:
        if headL1.val < headL2.val:
            headL3.next= ListNode(headL1.val)
            headL1 = headL1.next
        else:
            headL3.next = ListNode(headL2.val)
            headL2 = headL2.next
        headL3 = headL3.next
    if headL1:
        headL3.next = headL1
    else:
        headL3.next = headL2
    return result.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

solution(l1,l2)