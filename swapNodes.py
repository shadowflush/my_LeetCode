class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def solution(head):
    if not head or not head.next:
        return head
    odd, even, head1 = head, head.next, head.next
    while head1.next:
        head.next,head = head1.next,head.next
        if head.next:
            head1.next,head1 = head.next,head1.next
    head.next, head = None, even
    while even.next:
        even.next,even,odd.next,odd = odd,even.next, even.next, odd.next
    even.next = odd
    return head






l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)


h = solution(l1)
while h:
    print(h.val)
    h = h.next

