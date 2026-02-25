import unittest
from collections import deque


# time:  O(nm)
# space: O(nm)
# where: n = len(grid), m = len(grid[0])
def best_bridge(grid: list[list[str]]) -> int:  # ty: ignore[invalid-return-type]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != "L":
                continue
            island = _cells_in_island(grid, y, x)
            return _steps_to_next_island(grid, island)


def _cells_in_island(grid: list[list[str]], y: int, x: int) -> set[tuple[int, int]]:
    visited = {(y, x)}
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            yp, xp = y + dy, x + dx
            if (
                0 <= yp < len(grid)
                and 0 <= xp < len(grid[0])
                and (yp, xp) not in visited
                and grid[yp][xp] == "L"
            ):
                visited.add((yp, xp))
                stack.append((yp, xp))
    return visited


def _steps_to_next_island(grid: list[list[str]], island: set[tuple[int, int]]) -> int:  # ty: ignore[invalid-return-type]
    queue = deque([(y, x, 0) for y, x in island])
    while queue:
        y, x, steps = queue.popleft()
        if (y, x) not in island and grid[y][x] == "L":
            return steps - 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            yp, xp = y + dy, x + dx
            if (
                0 <= yp < len(grid)
                and 0 <= xp < len(grid[0])
                and (yp, xp) not in island
            ):
                queue.append((yp, xp, steps + 1))


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [
            ["W", "W", "W", "L", "L"],
            ["L", "L", "W", "W", "L"],
            ["L", "L", "L", "W", "L"],
            ["W", "L", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
        ]
        self.assertEqual(best_bridge(grid), 1)

    def test_01(self) -> None:
        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["L", "L", "W", "W", "L"],
            ["W", "L", "W", "W", "L"],
            ["W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W"],
        ]
        self.assertEqual(best_bridge(grid), 2)

    def test_02(self) -> None:
        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "L", "W"],
            ["L", "W", "W", "W", "W"],
        ]
        self.assertEqual(best_bridge(grid), 3)

    def test_03(self) -> None:
        grid = [
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "L", "W"],
            ["W", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "L", "L", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        self.assertEqual(best_bridge(grid), 3)

    def test_04(self) -> None:
        grid = [
            ["L", "L", "L", "L", "L", "L", "L", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "L", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "L", "L", "L", "L", "L", "L", "L"],
        ]
        self.assertEqual(best_bridge(grid), 2)

    def test_05(self) -> None:
        grid = [
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W", "W", "W", "L"],
        ]
        self.assertEqual(best_bridge(grid), 8)


if __name__ == "__main__":
    unittest.main()
