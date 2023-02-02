from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        countDict = dict()
        for num in nums:
            if countDict.keys().__contains__(num):
                countDict[num] = countDict[num]+1
            else:
                countDict[num] = 1
            if countDict[num] == len(nums)/2:
                return num

        # for key in countDict.keys():
        #     if countDict[key] == len(nums)/2:
        #         return key

        return -1

sol = Solution()
print(sol.repeatedNTimes([1,2,3,3]))
print(sol.repeatedNTimes([2,1,2,5,3,2]))
print(sol.repeatedNTimes([5,1,5,2,5,3,5,4]))
