class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + " -> " + str(self.next)


def from_list(ls: list[int]) -> ListNode:
    if ls:
        val, *tail = ls
        node = ListNode(val)
        if len(tail) > 0:
            node.next = from_list(tail)
    return node


def to_list(ln: ListNode | None) -> list[int]:
    if ln is None:
        return []
    return [ln.val, *to_list(ln.next)]


def concat_to_int(ls: list[int]) -> int:
    return int("".join(map(str, ls)))


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        r1 = concat_to_int(to_list(l1))
        r2 = concat_to_int(to_list(l2))
        print(r1, r2)
        r = r1 + r2
        return from_list(reversed(list(map(int, list(str(r))))))


def main():
    l1 = from_list([2, 4, 9])
    l2 = from_list([5, 6, 4, 9])
    sol = Solution()
    r = sol.addTwoNumbers(l1, l2)
    print(r)


if __name__ == "__main__":
    main()
