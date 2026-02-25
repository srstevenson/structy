import unittest
from typing import Final

DIRECTIONS: Final = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# time:  O(nm4ˡ)
# space: O(l)
# where: n = len(grid), m = len(grid[0]), l = len(s)
def string_search(grid: list[list[str]], s: str) -> bool:
    def _dfs(row: int, col: int, seen: set[tuple[int, int]], idx: int) -> bool:
        if idx == len(s):
            return True
        for drow, dcol in DIRECTIONS:
            if (
                0 <= (rowp := row + drow) < len(grid)
                and 0 <= (colp := col + dcol) < len(grid[0])
                and (rowp, colp) not in seen
                and grid[rowp][colp] == s[idx]
            ):
                seen.add((rowp, colp))  # ty: ignore[possibly-unresolved-reference]
                if _dfs(rowp, colp, seen, idx + 1):  # ty: ignore[possibly-unresolved-reference]
                    return True
                seen.remove((rowp, colp))  # ty: ignore[possibly-unresolved-reference]
        return False

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == s[0] and _dfs(row, col, {(row, col)}, 1):
                return True
    return False


class TestSolution(unittest.TestCase):
    def test_00(self) -> None:
        grid = [
            ["e", "y", "h", "i", "j"],
            ["q", "x", "e", "r", "p"],
            ["r", "o", "l", "l", "n"],
            ["p", "r", "x", "o", "h"],
            ["a", "a", "m", "c", "m"],
        ]
        self.assertTrue(string_search(grid, "hello"))

    def test_01(self) -> None:
        grid = [
            ["e", "y", "h", "i", "j"],
            ["q", "x", "e", "r", "p"],
            ["r", "o", "l", "l", "n"],
            ["p", "r", "x", "o", "h"],
            ["a", "a", "m", "c", "m"],
        ]
        self.assertTrue(string_search(grid, "proxy"))

    def test_02(self) -> None:
        grid = [
            ["e", "y", "h", "i", "j"],
            ["q", "x", "e", "r", "p"],
            ["r", "o", "l", "l", "n"],
            ["p", "r", "x", "o", "h"],
            ["a", "a", "m", "c", "m"],
        ]
        self.assertFalse(string_search(grid, "rolling"))

    def test_03(self) -> None:
        grid = [
            ["e", "y", "h", "i", "j"],
            ["q", "x", "e", "r", "p"],
            ["r", "o", "l", "l", "n"],
            ["p", "r", "x", "o", "h"],
            ["a", "a", "m", "z", "m"],
        ]
        self.assertFalse(string_search(grid, "zoo"))

    def test_04(self) -> None:
        grid = [
            ["q", "w", "h", "i", "j"],
            ["q", "e", "r", "o", "p"],
            ["h", "y", "t", "x", "z"],
            ["k", "o", "m", "o", "p"],
        ]
        self.assertTrue(string_search(grid, "qwerty"))

    def test_05(self) -> None:
        grid = [
            ["f", "d", "i", "e", "l", "u", "j", "t", "q", "v", "o", "p"],
            ["o", "p", "b", "e", "m", "w", "m", "l", "h", "j", "s", "v"],
            ["g", "b", "s", "m", "i", "w", "w", "h", "l", "m", "l", "n"],
            ["a", "l", "s", "k", "p", "c", "t", "u", "v", "b", "c", "m"],
            ["m", "t", "c", "k", "e", "n", "r", "b", "a", "z", "l", "c"],
            ["q", "m", "a", "p", "a", "p", "i", "i", "u", "t", "z", "z"],
            ["d", "u", "z", "o", "e", "r", "a", "t", "t", "c", "q", "k"],
            ["f", "u", "z", "g", "c", "i", "k", "v", "o", "f", "s", "w"],
            ["p", "h", "u", "i", "k", "c", "v", "v", "h", "q", "v", "i"],
            ["l", "q", "w", "f", "y", "g", "w", "f", "a", "u", "x", "q"],
        ]
        self.assertTrue(string_search(grid, "paprika"))

    def test_06(self) -> None:
        grid = [
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "s", "s"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "x", "x"],
            ["s", "s", "s", "s", "s", "s", "s", "s", "s", "x", "h"],
        ]
        self.assertFalse(string_search(grid, "ssssssssssh"))

    def test_07(self) -> None:
        grid = [["a", "b", "a"], ["t", "x", "x"], ["x", "x", "x"]]
        self.assertTrue(string_search(grid, "abat"))

    def test_08(self) -> None:
        grid = [
            ["a", "o", "o", "o", "o"],
            ["b", "c", "d", "o", "o"],
            ["c", "f", "e", "o", "o"],
            ["d", "o", "o", "o", "o"],
            ["o", "o", "o", "o", "o"],
        ]
        self.assertTrue(string_search(grid, "abcdefc"))


if __name__ == "__main__":
    unittest.main()
