from pprint import pprint
from typing import List


class Solution:
    soldiersByRow = dict();
    rowsOrderedBySoldiers = list();

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        self.soldiersByRow = dict();
        self.rowsOrderedBySoldiers = list();
        for rowInd, row in enumerate(mat):
            self.soldiersByRow[rowInd] = 0;
            for cell in row:
                if cell == 1:
                    self.soldiersByRow[rowInd] += 1;
        #pprint(self.soldiersByRow);

        for rows in self.soldiersByRow:
            least = 500;
            leastRow = -1;
            for key, v in self.soldiersByRow.items():
                if v >= 0 and v < least:
                    least = v;
                    leastRow = key;
            self.rowsOrderedBySoldiers.append(leastRow);
            self.soldiersByRow[leastRow] = -1;

            if len(self.rowsOrderedBySoldiers) == k:
                return self.rowsOrderedBySoldiers;

        print(self.rowsOrderedBySoldiers);
        return None;


sol = Solution();
print(sol.kWeakestRows([[1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0],
                        [1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1]], 3));

print(sol.kWeakestRows([[1, 0, 0, 0],
                        [1, 1, 1, 1],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]], 2));
