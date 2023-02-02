from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for ind, elem in enumerate (arr):
            if ind == elem:
                return ind
        return -1

sol = Solution()
print(sol.fixedPoint([-10,-5,0,3,7]))
print(sol.fixedPoint([0,2,5,8,17]))
print(sol.fixedPoint([-10,-5,3,4,7,9]))
