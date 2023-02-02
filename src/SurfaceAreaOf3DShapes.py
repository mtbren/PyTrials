from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        totalArea = 0;
        for row, rowVal in enumerate(grid):
            for col, colVal in enumerate(rowVal):
                facesToRemove = 0;

                # Previous row  - Same column
                if row > 0:
                    facesToRemove += min(grid[row][col], grid[row - 1][col]);

                # Same row - Previous column
                if col > 0:
                    facesToRemove += min(grid[row][col], grid[row][col - 1]);

                # Next row  - Same column
                if row < len(grid) - 1:
                    facesToRemove += min(grid[row][col], grid[row + 1][col]);

                # Same row - Next column
                if col < len(grid[row]) - 1:
                    facesToRemove += min(grid[row][col], grid[row][col + 1]);

                if grid[row][col] > 0:
                    totalArea += (4 * grid[row][col] + 2 - facesToRemove);

        return totalArea;


sol = Solution();
print(sol.surfaceArea([[1,2],[3,4]])); #34
print(sol.surfaceArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]])); #32
print(sol.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]])); #46

