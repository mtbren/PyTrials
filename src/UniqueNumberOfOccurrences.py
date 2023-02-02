from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numberToOccurrences = dict()
        occurrencesToNumber = dict()
        for number in arr:
            if number in numberToOccurrences.keys():
                numberToOccurrences[number] = numberToOccurrences[number] + 1
            else:
                numberToOccurrences[number] = 1

        for number in numberToOccurrences.keys():
            if numberToOccurrences[number] in occurrencesToNumber.keys():
                return False
            else:
                occurrencesToNumber[numberToOccurrences[number]] = 1

        return True


sol = Solution()
print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
print(sol.uniqueOccurrences([1, 2]))  # False
print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # True
