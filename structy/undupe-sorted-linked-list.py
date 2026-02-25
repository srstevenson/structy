import unittest


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def undupe_sorted_linked_list(head: Node) -> Node:
    unduped = Node(head.val)
    current = unduped
    while head:
        if head.val != current.val:
            current.next = Node(head.val)
            current = current.next
        head = head.next  # ty: ignore[invalid-assignment]
    return unduped


class TestSolution(unittest.TestCase):
    def values_of(self, head: Node | None) -> list[int]:
        values: list[int] = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_00(self) -> None:
        a = Node(4)
        b = Node(4)
        c = Node(6)
        d = Node(6)
        e = Node(6)
        f = Node(7)
        g = Node(7)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        f.next = g

        self.assertEqual(self.values_of(undupe_sorted_linked_list(a)), [4, 6, 7])

    def test_01(self) -> None:
        w = Node(5)
        x = Node(5)
        y = Node(5)
        z = Node(8)

        w.next = x
        x.next = y
        y.next = z

        self.assertEqual(self.values_of(undupe_sorted_linked_list(x)), [5, 8])

    def test_02(self) -> None:
        p = Node(10)
        q = Node(20)
        r = Node(30)

        p.next = q
        q.next = r
        self.assertEqual(self.values_of(undupe_sorted_linked_list(p)), [10, 20, 30])


if __name__ == "__main__":
    unittest.main()
