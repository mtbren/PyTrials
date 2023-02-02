class Solution:
    def tribonacci(self, n: int) -> int:
        tribList = [0, 1, 1];
        if n == 0:
            return 0;
        elif n == 1:
            return 1;
        elif n == 2:
            return 1;
        else:
            for i in range(3, n + 1):
                tribI = tribList[i - 3] + tribList[i - 2] + tribList[i - 1];
                tribList.append(tribI);
            return tribList[n];


sol = Solution();
print(sol.tribonacci(3));
print(sol.tribonacci(4));
print(sol.tribonacci(5));
print(sol.tribonacci(25));
print(sol.tribonacci(37));
