class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        if month in [1,3,5,7,8,10,12]:
            return 31;
        elif month in [4,6,9,11]:
            return 30;
        elif month == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return 29;
                    else:
                        return 28;
                else:
                    return 29;
            elif year % 4 != 0:
                return 28;

sol = Solution();
print(sol.numberOfDays(1992, 7));
print(sol.numberOfDays(2000, 2));
print(sol.numberOfDays(1900, 2));
