import unittest


class Node:
    def __init__(self, val: str) -> None:
        self.val: str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def flatten_tree(root: Node) -> Node:
    previous = None
    stack = [root]
    while stack:
        current = stack.pop()

        if previous:
            previous.right = current

        previous = current

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

        current.left = current.right = None

    return root


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        a = flatten_tree(a)
        self.assertIsNone(a.left)
        self.assertEqual(a.right.val, "b")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.val, "d")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.val, "e")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.val, "c")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.right.val, "f")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.right.val, "f")  # ty: ignore[unresolved-attribute]
        self.assertIsNone(a.right.right.right.right.right.right)  # ty: ignore[unresolved-attribute]

    def test_01(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        e = Node("e")

        a.left = b
        a.right = c
        b.right = e

        a = flatten_tree(a)
        self.assertIsNone(a.left)
        self.assertEqual(a.right.val, "b")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.val, "e")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.val, "c")  # ty: ignore[unresolved-attribute]
        self.assertIsNone(a.right.right.right.right)  # ty: ignore[unresolved-attribute]

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")

        a.left = b
        a.right = c
        b.left = d
        d.left = e
        e.left = f
        f.left = g

        a = flatten_tree(a)
        self.assertIsNone(a.left)
        self.assertEqual(a.right.val, "b")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.val, "d")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.val, "e")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.val, "f")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.right.val, "g")  # ty: ignore[unresolved-attribute]
        self.assertEqual(a.right.right.right.right.right.right.val, "c")  # ty: ignore[unresolved-attribute]
        self.assertIsNone(a.right.right.right.right.right.right.right)  # ty: ignore[unresolved-attribute]


if __name__ == "__main__":
    unittest.main()
