# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if(self.next == None) :
            return(str(self.val))
        else :
            return(str(self.val) + ' -> ' + str(self.next))

def toNum(l : ListNode) -> int:
    def loop(acc : int, lp : ListNode, multp : int) -> int :
        if not lp :
            return(acc)
        else :
            return(loop(acc + lp.val * multp, lp.next, multp * 10))
    return(loop(acc = 0, lp = l, multp = 1))

def listToNode(l : list) -> ListNode:
    x, *xs = l
    L_ret = ListNode(x)
    if not xs:
        return(L_ret)
    else :
        L_ret.next = listToNode(xs)
    return(L_ret)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = toNum(l1) + toNum(l2)
        string_x_rev = reversed(str(x))
        toNode = lambda y : listToNode(list(map(int, string_x_rev)))
        return(toNode(x))

