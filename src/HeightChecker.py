from typing import List


class HeightChecker:
    def checkHeight(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights);
        countOutOfOrder = 0;
        for ind, val in enumerate(heights):
            if val != sortedHeights[ind]:
                countOutOfOrder += 1;
        return countOutOfOrder;

checker = HeightChecker();
print(checker.checkHeight([1,1,4,2,1,3])); #3
print(checker.checkHeight([5,1,2,3,4])); #5
print(checker.checkHeight([1,2,3,4,5])); #0