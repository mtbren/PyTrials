from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        kTotalCal = 0;
        kTotalPoints = 0;
        for ind, cal in enumerate(calories):
            if ind < k - 1:
                kTotalCal += cal;
            else:
                kTotalCal += cal;
                if kTotalCal < lower:
                    kTotalPoints -= 1;
                elif kTotalCal > upper:
                    kTotalPoints += 1;
                kTotalCal -= calories[ind - k + 1];
        return kTotalPoints;


sol = Solution();
print(sol.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3));
print(sol.dietPlanPerformance([3, 2], 2, 0, 1));
print(sol.dietPlanPerformance([6, 5, 0, 0], 2, 1, 5));
