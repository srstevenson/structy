import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def linked_list_cycle(head: Node | None) -> bool:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next  # ty: ignore[unresolved-attribute]
        if fast is slow:
            return True
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d
        d.next = b  # cycle

        self.assertTrue(linked_list_cycle(a))

    def test_01(self) -> None:
        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")

        q.next = r
        r.next = s
        s.next = t
        t.next = u
        u.next = q  # cycle

        self.assertTrue(linked_list_cycle(q))

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertFalse(linked_list_cycle(a))

    def test_03(self) -> None:
        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")

        q.next = r
        r.next = s
        s.next = t
        t.next = u
        u.next = t  # cycle

        self.assertTrue(linked_list_cycle(q))

    def test_04(self) -> None:
        p = Node("p")

        self.assertFalse(linked_list_cycle(p))

    def test_05(self) -> None:
        self.assertFalse(linked_list_cycle(None))


if __name__ == "__main__":
    unittest.main()
