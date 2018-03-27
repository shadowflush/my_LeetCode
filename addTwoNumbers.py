class ListNote:
    def __init__(self,x):
        self.data = x
        self.next = None

def addTwoNumbers(L1,L2):
    carry = 0
    new_list = tmp = ListNote(0)
    while L1 or L2 or carry:
        if L1:
            carry += L1.data
            L1 = L1.next
        if L2:
            carry += L2.data
            L2 = L2.next
        carry , tmp.data = divmod(carry,10)
        if L1 or L2 or carry:
            tmp.next = ListNote(0)
            tmp = tmp.next
    return new_list

a = ListNote(3)
a.next = ListNote(0)
a.next.next = ListNote(8)
b = ListNote(4)
b.next = ListNote(3)
b.next.next = ListNote(8)
c = addTwoNumbers(a,b)

