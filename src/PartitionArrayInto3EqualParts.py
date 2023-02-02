from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum = 0;
        for item in arr:
            sum += item;

        if sum % 3 != 0:
            return False;
        else:
            expectedPartitionSum = sum // 3;
            actualPartitionSum1 = 0;
            for index1, item1 in enumerate(arr):
                actualPartitionSum1 += item1;
                if actualPartitionSum1 == expectedPartitionSum:
                    actualPartitionSum2 = 0;
                    for index2 in range(index1+1, len(arr)):
                        actualPartitionSum2 += arr[index2];
                        if actualPartitionSum2 == expectedPartitionSum:
                            if index2 != len(arr)-1:
                                return True;

            return False;

sol = Solution();
print(sol.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]));    #True
print(sol.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]));    #False
print(sol.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]));      #True