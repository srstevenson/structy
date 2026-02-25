import sys
import unittest
from collections import defaultdict, deque
from typing import Final

DIRECTIONS: Final = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# time:  O(n²m²)
# space: O(n²m²)
# where: where: n = len(grid), m = len(grid[0])
def best_house_build(grid: list[list[int]]) -> int:
    distances: defaultdict[tuple[int, int], int] = defaultdict(int)
    visited: defaultdict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    queue: deque[tuple[int, int, int, int, int]] = deque()

    houses = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                houses += 1
                visited[(row, col)].add((row, col))
                queue.append((row, col, row, col, 0))

    while queue:
        row, col, start_row, start_col, distance = queue.popleft()
        for drow, dcol in DIRECTIONS:
            if (
                0 <= (rowp := row + drow) < len(grid)
                and 0 <= (colp := col + dcol) < len(grid[0])
                and (start_row, start_col) not in visited[(rowp, colp)]
                and grid[rowp][colp] == 0
            ):
                visited[(rowp, colp)].add((start_row, start_col))  # ty: ignore[possibly-unresolved-reference]
                queue.append((rowp, colp, start_row, start_col, distance + 1))  # ty: ignore[possibly-unresolved-reference]
                distances[(rowp, colp)] += distance + 1  # ty: ignore[possibly-unresolved-reference]

    min_distance = sys.maxsize
    for cell in visited:
        if len(visited[cell]) == houses and distances[cell] > 0:
            min_distance = min(min_distance, distances[cell])

    return min_distance if min_distance < sys.maxsize else -1


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(best_house_build(grid), 6)

    def test_01(self) -> None:
        grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(best_house_build(grid), 7)

    def test_02(self) -> None:
        grid = [
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(best_house_build(grid), 8)

    def test_03(self) -> None:
        grid = [
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ]
        self.assertEqual(best_house_build(grid), 11)

    def test_04(self) -> None:
        grid = [
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 1, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1],
        ]
        self.assertEqual(best_house_build(grid), 13)

    def test_05(self) -> None:
        grid = [
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1],
        ]
        self.assertEqual(best_house_build(grid), -1)

    def test_06(self) -> None:
        grid = [[1, 0]]
        self.assertEqual(best_house_build(grid), 1)


if __name__ == "__main__":
    unittest.main()
