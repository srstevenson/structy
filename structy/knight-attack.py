import unittest
from collections import deque
from typing import Final

DIRECTIONS: Final = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
]


# time:  O(n²)
# space: O(n²)
def knight_attack(n: int, kr: int, kc: int, pr: int, pc: int) -> int | None:
    seen = {(kr, kc)}
    queue = deque([(kr, kc, 0)])

    while queue:
        kr, kc, moves = queue.popleft()
        if kr == pr and kc == pc:
            return moves
        for dr, dc in DIRECTIONS:
            if (
                0 <= (krp := kr + dr) < n
                and 0 <= (kcp := kc + dc) < n
                and (krp, kcp) not in seen
            ):
                seen.add((krp, kcp))  # ty: ignore[possibly-unresolved-reference]
                queue.append((krp, kcp, moves + 1))  # ty: ignore[possibly-unresolved-reference]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(knight_attack(8, 1, 1, 2, 2), 2)

    def test_01(self) -> None:
        self.assertEqual(knight_attack(8, 1, 1, 2, 3), 1)

    def test_02(self) -> None:
        self.assertEqual(knight_attack(8, 0, 3, 4, 2), 3)

    def test_03(self) -> None:
        self.assertEqual(knight_attack(8, 0, 3, 5, 2), 4)

    def test_04(self) -> None:
        self.assertEqual(knight_attack(24, 4, 7, 19, 20), 10)

    def test_05(self) -> None:
        self.assertEqual(knight_attack(100, 21, 10, 0, 0), 11)

    def test_06(self) -> None:
        self.assertEqual(knight_attack(3, 0, 0, 1, 2), 1)

    def test_07(self) -> None:
        self.assertIsNone(knight_attack(3, 0, 0, 1, 1))


if __name__ == "__main__":
    unittest.main()
