import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(min(n, m))
# space: O(1)
# where: n = number of nodes in head_1, m = number of nodes in head_2
def merge_lists(head_1: Node, head_2: Node) -> Node:
    if head_1.val < head_2.val:
        head = tail = head_1
        head_1: Node | None = head_1.next
    else:
        head = tail = head_2
        head_2: Node | None = head_2.next

    while head_1 and head_2:
        if head_1.val < head_2.val:
            tail.next = head_1
            head_1 = head_1.next  # ty: ignore[conflicting-declarations]
        else:
            tail.next = head_2
            head_2 = head_2.next  # ty: ignore[conflicting-declarations]
        tail = tail.next

    if head_1:
        tail.next = head_1
    elif head_2:
        tail.next = head_2

    return head


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[int]:
        values: list[int] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        a = Node(5)
        b = Node(7)
        c = Node(10)
        d = Node(12)
        e = Node(20)
        f = Node(28)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        q = Node(6)
        r = Node(8)
        s = Node(9)
        t = Node(25)
        q.next = r
        r.next = s
        s.next = t

        self.assertEqual(
            self.values_of(merge_lists(a, q)), [5, 6, 7, 8, 9, 10, 12, 20, 25, 28]
        )

    def test_01(self) -> None:
        a = Node(5)
        b = Node(7)
        c = Node(10)
        d = Node(12)
        e = Node(20)
        f = Node(28)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        q = Node(1)
        r = Node(8)
        s = Node(9)
        t = Node(10)
        q.next = r
        r.next = s
        s.next = t

        self.assertEqual(
            self.values_of(merge_lists(a, q)), [1, 5, 7, 8, 9, 10, 10, 12, 20, 28]
        )

    def test_02(self) -> None:
        h = Node(30)

        p = Node(15)
        q = Node(67)
        p.next = q

        self.assertEqual(self.values_of(merge_lists(h, p)), [15, 30, 67])


if __name__ == "__main__":
    unittest.main()
