from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenPtr = 0;
        oddPtr = 1;
        while True:
            if nums[evenPtr] % 2 != 0: #not even
                if nums[oddPtr] % 2 != 1: #not odd
                    temp = nums[oddPtr];
                    nums[oddPtr] = nums[evenPtr];
                    nums[evenPtr] = temp;
                else:
                    oddPtr = oddPtr + 2;
            else:
                evenPtr = evenPtr + 2;
            if evenPtr >= len(nums) or oddPtr >= len(nums):
                break;
        return nums;


sol = Solution();
print(sol.sortArrayByParityII([4, 2, 5, 7]));
print(sol.sortArrayByParityII([2,3]));
print(sol.sortArrayByParityII([3,2]));
print(sol.sortArrayByParityII([3,1,4,2]));


