import unittest


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.next: Node | None = None


# time:  O(n)
# space: O(1)
# where: n = number of nodes
def is_univalue_list(head: Node) -> bool:
    val = head.val
    while head:
        if head.val != val:
            return False
        head: Node | None = head.next
    return True


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node(7)
        b = Node(7)
        c = Node(7)

        a.next = b
        b.next = c

        self.assertTrue(is_univalue_list(a))

    def test_01(self) -> None:
        a = Node(7)
        b = Node(7)
        c = Node(4)

        a.next = b
        b.next = c

        self.assertFalse(is_univalue_list(a))

    def test_02(self) -> None:
        u = Node(2)
        v = Node(2)
        w = Node(2)
        x = Node(2)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        self.assertTrue(is_univalue_list(u))

    def test_03(self) -> None:
        u = Node(2)
        v = Node(2)
        w = Node(3)
        x = Node(3)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        self.assertFalse(is_univalue_list(u))

    def test_04(self) -> None:
        z = Node("z")

        self.assertTrue(is_univalue_list(z))

    def test_05(self) -> None:
        u = Node(2)
        v = Node(1)
        w = Node(2)
        x = Node(2)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        self.assertFalse(is_univalue_list(u))


if __name__ == "__main__":
    unittest.main()
