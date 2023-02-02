from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        sortedWeight = sorted(weight)
        remainingWeight = 0
        countInBasket = 0
        for apple in sortedWeight:
            if (remainingWeight+apple) <= 5000:
                countInBasket += 1
                remainingWeight += apple
            else:
                break

        return countInBasket


sol = Solution()
print(sol.maxNumberOfApples([100,200,150,1000]))
print(sol.maxNumberOfApples([900,950,800,1000,700,800]))