from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        retList = [];
        for rowInd, rowVal in enumerate(matrix):
            for colInd, colVal in enumerate(rowVal):
                if len(retList) < colInd+1:
                    retList.append([]);
                retList[colInd].append(colVal);

        return retList;

sol = Solution();
#print(sol.transpose([[1, 2], [3, 4]]));
print(sol.transpose([1]));