import unittest
from functools import cache
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


# time:  O(n²m)
# space: O(n²m)
def knightly_number(n: int, m: int, kr: int, kc: int, pr: int, pc: int) -> int:  # noqa: PLR0913
    @cache
    def _knightly_number(m: int, kr: int, kc: int) -> int:
        if m == 0:
            return 1 if kr == pr and kc == pc else 0

        return sum(
            _knightly_number(m - 1, krp, kcp)  # ty: ignore[possibly-unresolved-reference]
            for dr, dc in DIRECTIONS
            if 0 <= (krp := kr + dr) < n and 0 <= (kcp := kc + dc) < n
        )

    return _knightly_number(m, kr, kc)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(knightly_number(8, 2, 4, 4, 5, 5), 2)

    def test_01(self) -> None:
        self.assertEqual(knightly_number(8, 2, 7, 1, 7, 1), 3)

    def test_02(self) -> None:
        self.assertEqual(knightly_number(8, 2, 5, 4, 5, 4), 8)

    def test_03(self) -> None:
        self.assertEqual(knightly_number(8, 3, 5, 2, 4, 4), 21)

    def test_04(self) -> None:
        self.assertEqual(knightly_number(20, 6, 18, 7, 10, 15), 60)

    def test_05(self) -> None:
        self.assertEqual(knightly_number(20, 12, 8, 3, 9, 14), 98410127)

    def test_06(self) -> None:
        self.assertEqual(knightly_number(8, 2, 0, 0, 1, 1), 0)


if __name__ == "__main__":
    unittest.main()
