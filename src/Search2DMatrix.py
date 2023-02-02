from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix);
        #cols = len(rows);
        rowNum = self.searchMatrixRows(matrix, target, 0, rows-1);
        print(rowNum);

    def searchMatrixRows(self, matrix: List[List[int]], target: int, beginIndex: int, endIndex: int) -> int:
        totalRows = endIndex - beginIndex + 1;
        if totalRows <= 1:
            return beginIndex;

        row = int(totalRows/2);
        if totalRows == 2:
            if matrix[row+1][0] > target :
                return row+1;
            elif matrix[row+1][0] < target:
                return row;
        if matrix[row][0] < target:
            beginIndex = row;
            return self.searchMatrixRows(matrix, target, beginIndex, endIndex);
        elif matrix[row][0] > target:
            endIndex = row;
            return self.searchMatrixRows(matrix, target, beginIndex, endIndex);
        else:
            return row;


sol = Solution();
sol.searchMatrix([[1, 3, 5, 7],
                  [10, 11, 16, 20],
                  [23, 30, 34, 60]], 30);
