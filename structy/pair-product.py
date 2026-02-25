import unittest


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def pair_product(numbers: list[int], target_product: int) -> tuple[int, int]:  # ty: ignore[invalid-return-type]
    seen: dict[int, int] = {}
    for idx, number in enumerate(numbers):
        if (required := target_product // number) in seen:
            return seen[required], idx
        seen[number] = idx


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(pair_product([3, 2, 5, 4, 1], 8), (1, 3))

    def test_01(self) -> None:
        self.assertEqual(pair_product([3, 2, 5, 4, 1], 10), (1, 2))

    def test_02(self) -> None:
        self.assertEqual(pair_product([4, 7, 9, 2, 5, 1], 5), (4, 5))

    def test_03(self) -> None:
        self.assertEqual(pair_product([4, 7, 9, 2, 5, 1], 35), (1, 4))

    def test_04(self) -> None:
        self.assertEqual(pair_product([3, 2, 5, 4, 1], 10), (1, 2))

    def test_05(self) -> None:
        self.assertEqual(pair_product([4, 6, 8, 2], 16), (2, 3))

    def test_06(self) -> None:
        numbers = list(range(1, 6001))
        self.assertEqual(pair_product(numbers, 35994000), (5998, 5999))


if __name__ == "__main__":
    unittest.main()
