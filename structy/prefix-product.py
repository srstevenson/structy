import unittest


# time:  O(n)
# space: O(n)
# where: n = len(numbers)
def prefix_product(numbers: list[int]) -> list[int]:
    product = 1
    return [(product := product * num) for num in numbers]  # ty: ignore[unresolved-reference]


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        self.assertEqual(prefix_product([4, 2, 1, 6, 3, 6]), [4, 8, 8, 48, 144, 864])

    def test_01(self) -> None:
        self.assertEqual(prefix_product([10, 5, -2, 1, 1]), [10, 50, -100, -100, -100])

    def test_02(self) -> None:
        self.assertEqual(prefix_product([2, 5]), [2, 10])

    def test_03(self) -> None:
        self.assertEqual(
            prefix_product([12, 88, 0, -50, 30, 2]), [12, 1056, 0, 0, 0, 0]
        )

    def test_04(self) -> None:
        self.assertEqual(prefix_product([2]), [2])


if __name__ == "__main__":
    unittest.main()
