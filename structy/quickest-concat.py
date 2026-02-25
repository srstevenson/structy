import sys
import unittest
from functools import cache


# time:  O(nm)
# space: O(n)
# where: n = len(s), m = len(words)
def quickest_concat(s: str, words: list[str]) -> int:
    @cache
    def _quickest_concat(idx: int) -> int:
        if idx == len(s):
            return 0

        min_count = sys.maxsize
        for word in words:
            if (
                s.startswith(word, idx)
                and (count := _quickest_concat(idx + len(word))) > -1
            ):
                min_count = min(min_count, count + 1)  # ty: ignore[possibly-unresolved-reference]

        return min_count if min_count < sys.maxsize else -1

    return _quickest_concat(0)


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(quickest_concat("caution", ["ca", "ion", "caut", "ut"]), 2)

    def test_01(self) -> None:
        self.assertEqual(quickest_concat("caution", ["ion", "caut", "caution"]), 1)

    def test_02(self) -> None:
        self.assertEqual(
            quickest_concat("respondorreact", ["re", "or", "spond", "act", "respond"]),
            4,
        )

    def test_03(self) -> None:
        self.assertEqual(
            quickest_concat("simchacindy", ["sim", "simcha", "acindy", "ch"]), 3
        )

    def test_04(self) -> None:
        self.assertEqual(
            quickest_concat("simchacindy", ["sim", "simcha", "acindy"]), -1
        )

    def test_05(self) -> None:
        self.assertEqual(quickest_concat("uuuuuu", ["u", "uu", "uuu", "uuuu"]), 2)

    def test_06(self) -> None:
        self.assertEqual(quickest_concat("rongbetty", ["wrong", "bet"]), -1)

    def test_07(self) -> None:
        self.assertEqual(
            quickest_concat(
                "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", ["u", "uu", "uuu", "uuuu", "uuuuu"]
            ),
            7,
        )


if __name__ == "__main__":
    unittest.main()
