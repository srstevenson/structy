import unittest
from collections import Counter


# time:  O(n)
# space: O(n)
# where: n = len(s)
def most_frequent_char(s: str) -> str:
    counts = Counter(s)
    return max(counts, key=counts.get)  # ty: ignore[no-matching-overload]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(most_frequent_char("bookeeper"), "e")

    def test_01(self) -> None:
        self.assertEqual(most_frequent_char("david"), "d")

    def test_02(self) -> None:
        self.assertEqual(most_frequent_char("abby"), "b")

    def test_03(self) -> None:
        self.assertEqual(most_frequent_char("mississippi"), "i")

    def test_04(self) -> None:
        self.assertEqual(most_frequent_char("potato"), "o")

    def test_05(self) -> None:
        self.assertEqual(most_frequent_char("eleventennine"), "e")

    def test_06(self) -> None:
        self.assertEqual(most_frequent_char("riverbed"), "r")


if __name__ == "__main__":
    unittest.main()
