import functools as ft


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next:
            return str(self.val) + "->" + str(self.next.__repr__())
        return str(self.val)




class Solution:
    def merge2Linked(self, l1, l2):
        if not l1 and not l2:
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        x = l1.val
        y = l2.val
        if x <= y:
            ls = ListNode(x)
            ls.next = self.merge2Linked(l1.next, l2)
        else:
            ls = ListNode(y)
            ls.next = self.merge2Linked(l1, l2.next)
        return ls

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # Sort the List by value
        if lists:
            return ft.reduce(self.merge2Linked, lists)
        return ListNode("")


if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    s1 = ListNode(1)
    s2 = ListNode(3)
    s3 = ListNode(8)
    s4 = ListNode(9)
    s1.next = s2
    s2.next = s3
    s3.next = s4

    S = Solution()
    Y = S.mergeKLists([l4, s4, l3, l1, s1])
    print(Y)
