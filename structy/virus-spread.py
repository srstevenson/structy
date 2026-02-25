import unittest
from collections import deque
from typing import Final

DIRECTIONS: Final = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# time:  O(nm)
# space: O(nm)
# where: n = len(grid), m = len(grid[0])
def virus_spread(grid: list[list[int]]) -> int:
    num_clean = 0
    queue: deque[tuple[int, int, int]] = deque()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                num_clean += 1
            elif grid[row][col] == 2:
                queue.append((row, col, 0))

    time = 0
    while queue:
        row, col, time = queue.popleft()
        for dr, dc in DIRECTIONS:
            if (
                0 <= (rowp := row + dr) < len(grid)
                and 0 <= (colp := col + dc) < len(grid[0])
                and grid[rowp][colp] == 1
            ):
                grid[rowp][colp] = 2  # ty: ignore[possibly-unresolved-reference]
                num_clean -= 1
                queue.append((rowp, colp, time + 1))  # ty: ignore[possibly-unresolved-reference]

    return time if num_clean == 0 else -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [[1, 1, 1], [0, 1, 0], [0, 1, 2]]
        self.assertEqual(virus_spread(grid), 4)

    def test_01(self) -> None:
        grid = [[1, 0, 1], [0, 1, 0], [0, 1, 2]]
        self.assertEqual(virus_spread(grid), -1)

    def test_02(self) -> None:
        grid = [[0, 0, 0, 0, 1, 1, 2], [0, 1, 1, 1, 1, 1, 0], [0, 2, 0, 0, 0, 0, 0]]
        self.assertEqual(virus_spread(grid), 3)

    def test_03(self) -> None:
        grid = [
            [0, 0, 0, 0, 1, 1, 2],
            [0, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0],
        ]
        self.assertEqual(virus_spread(grid), -1)

    def test_04(self) -> None:
        grid = [
            [2, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 2, 2, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            [2, 1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(virus_spread(grid), 9)


if __name__ == "__main__":
    unittest.main()
