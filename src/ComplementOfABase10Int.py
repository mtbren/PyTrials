class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bitsOfN = str()
        bitsOfNComplement = str()
        while n >= 1:
            bitsOfN = str(n % 2) + bitsOfN
            n = n // 2

        for c in bitsOfN:
            if c == '1':
                bitsOfNComplement = bitsOfNComplement + '0'
            else:
                bitsOfNComplement = bitsOfNComplement + '1'

        ind = 0
        complement = 0
        for c in bitsOfNComplement[::-1]:
            if c == '1':
                complement = complement + pow(2, ind)
            ind += 1

        return complement


sol = Solution()
print(sol.bitwiseComplement(5))
print(sol.bitwiseComplement(7))
print(sol.bitwiseComplement(10))
