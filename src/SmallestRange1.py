from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0;
        sortedNums = sorted(nums);
        minNum = sortedNums[0];
        maxNum = sortedNums[len(sortedNums)-1];

        if maxNum - minNum < 2*k:
            return 0;
        else:
            return maxNum - minNum - 2*k;

sol = Solution();
print(sol.smallestRangeI([1],0));
print(sol.smallestRangeI([0,10],2));
print(sol.smallestRangeI([1,3,6],3));
