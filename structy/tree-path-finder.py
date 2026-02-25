import sys
import unittest
from typing import override


class Node:
    def __init__(self, val: int | str) -> None:
        self.val: int | str = val
        self.left: Node | None = None
        self.right: Node | None = None


# time:  O(n)
# space: O(n)
# where: n = number of nodes
def path_finder(root: Node | None, target: int | str) -> list[int | str] | None:
    def _path_finder(root: Node | None) -> list[int | str] | None:
        if root:
            if root.val == target:
                return [root.val]
            if root.left and (path := _path_finder(root.left)):
                path.append(root.val)  # ty: ignore[possibly-unresolved-reference]
                return path  # ty: ignore[possibly-unresolved-reference]
            if root.right and (path := _path_finder(root.right)):
                path.append(root.val)  # ty: ignore[possibly-unresolved-reference]
                return path  # ty: ignore[possibly-unresolved-reference]
        return None

    result = _path_finder(root)
    return result[::-1] if result else None


class TestSolution(unittest.TestCase):
    @override
    def setUp(self) -> None:
        sys.setrecursionlimit(20000)

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

        self.assertEqual(path_finder(a, "e"), ["a", "b", "e"])

    def test_01(self) -> None:
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

        self.assertIsNone(path_finder(a, "p"))

    def test_02(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(path_finder(a, "c"), ["a", "c"])

    def test_03(self) -> None:
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        self.assertEqual(path_finder(a, "h"), ["a", "c", "f", "h"])

    def test_04(self) -> None:
        x = Node("x")

        self.assertEqual(path_finder(x, "x"), ["x"])

    def test_05(self) -> None:
        self.assertIsNone(path_finder(None, "x"))

    def test_06(self) -> None:
        root = Node(0)
        curr = root
        for i in range(1, 19500):
            curr.right = Node(i)
            curr = curr.right

        result = path_finder(root, 16281)
        assert result  # For ty.
        self.assertEqual(result[0], 0)
        self.assertEqual(result[-1], 16281)
        self.assertEqual(len(result), 16282)


if __name__ == "__main__":
    unittest.main()
