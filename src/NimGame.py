class Solution:
    def canWinNim(self, n: int) -> bool:
        p1Playing = True;
        while True:
            if n <= 3:
                if p1Playing:
                    return True;
                else:
                    return False;
            else:
                if n > 6:
                    n -= 3;
                elif n == 6:
                    n -= 2;
                else:
                    n -= 1;

            p1Playing = not p1Playing;

sol = Solution();
print(sol.canWinNim(3)); #True
print(sol.canWinNim(5)); #True
print(sol.canWinNim(4)); #False
print(sol.canWinNim(1)); #True
print(sol.canWinNim(2)); #True
print(sol.canWinNim(7)); #True


