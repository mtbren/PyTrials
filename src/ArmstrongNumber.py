import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        strNum = str(n);
        listNum = list(strNum);
        length = len(listNum);

        sum = 0;
        for k in listNum:
            sum += math.pow(int(k), length);

        retBool = int(sum) == n;
        return retBool;


sol = Solution();
print(sol.isArmstrong(153));
print(sol.isArmstrong(123));
