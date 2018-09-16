class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def solution(head,k):
    def reversN(head,k):
        offset, p = k, head
        while offset and p:
            p = p.next
            offset -= 1
        if offset != 0:
            return head
        current,pre = head,None
        while offset < k:
            current.next, pre, current = pre, current, current.next
            offset += 1
        head.next = reversN(current,k)
        return pre
    return reversN(head,k)





l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)


h = solution(l1,5)
while h:
    print(h.val)
    h = h.next

