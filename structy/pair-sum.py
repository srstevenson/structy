import unittest


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def pair_sum(numbers: list[int], target_sum: int) -> tuple[int, int]:  # ty: ignore[invalid-return-type]
    seen: dict[int, int] = {}
    for idx, number in enumerate(numbers):
        if (diff := target_sum - number) in seen:
            return seen[diff], idx
        seen[number] = idx


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(pair_sum([3, 2, 5, 4, 1], 8), (0, 2))

    def test_01(self) -> None:
        self.assertEqual(pair_sum([4, 7, 9, 2, 5, 1], 5), (0, 5))

    def test_02(self) -> None:
        self.assertEqual(pair_sum([4, 7, 9, 2, 5, 1], 3), (3, 5))

    def test_03(self) -> None:
        self.assertEqual(pair_sum([1, 6, 7, 2], 13), (1, 2))

    def test_04(self) -> None:
        self.assertEqual(pair_sum([9, 9], 18), (0, 1))

    def test_05(self) -> None:
        self.assertEqual(pair_sum([6, 4, 2, 8], 12), (1, 3))

    def test_06(self) -> None:
        numbers = list(range(1, 6001))
        self.assertEqual(pair_sum(numbers, 11999), (5998, 5999))


if __name__ == "__main__":
    unittest.main()
