class Solution:
    def numberOfSteps(self, num: int) -> int:
        #origNum = num ;
        numOfSteps = 0;
        while num > 0:
            if num % 2 == 0:
                num = num // 2;
            else:
                num = num - 1;
            numOfSteps += 1 ;
        return numOfSteps;

sol = Solution();
print(sol.numberOfSteps(14));#6
print(sol.numberOfSteps(8));#4
print(sol.numberOfSteps(123));#12