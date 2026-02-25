import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def middle_value(head: Node) -> str:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next  # ty: ignore[unresolved-attribute]
    return slow.val  # ty: ignore[unresolved-attribute]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertEqual(middle_value(a), "c")

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual(middle_value(a), "d")

    def test_02(self) -> None:
        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z

        self.assertEqual(middle_value(x), "y")

    def test_03(self) -> None:
        x = Node("x")
        y = Node("y")

        x.next = y

        self.assertEqual(middle_value(x), "y")

    def test_04(self) -> None:
        q = Node("q")

        self.assertEqual(middle_value(q), "q")


if __name__ == "__main__":
    unittest.main()
