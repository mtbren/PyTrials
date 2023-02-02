from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        tempArr = arr.copy()
        while True:
            changed = False
            for index in range(1, len(arr) - 1):
                if arr[index] < arr[index - 1] and arr[index] < arr[index + 1]:
                    tempArr[index] = arr[index] + 1
                    changed = True
                if arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
                    tempArr[index] = arr[index] - 1
                    changed = True
            arr = tempArr.copy()
            if not changed:
                break
        return tempArr


sol = Solution()
print(sol.transformArray([2,1,2,1,1,2,2,1]))
print(sol.transformArray([6, 2, 3, 4]))
print(sol.transformArray([1,6,3,4,3,5]))