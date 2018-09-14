class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def solution(head, n):
    former = current = head
    while n > 0:
        current = current.next
        n -= 1
    if not current:
        head = head.next
        return head
    while current.next:
        former, current = former.next, current.next
    former.next = former.next.next
    return head

