class Solution:
    def binaryGap(self, n: int) -> int:
        bin = format(n, "b");
        lastSetBitIndex = -1;
        dist = 0;
        for bitIndex, bit in enumerate(bin):
            if bit == '1':
                if lastSetBitIndex == -1:
                    lastSetBitIndex = bitIndex;
                else:
                    dist = max(dist, bitIndex - lastSetBitIndex);
                    lastSetBitIndex = bitIndex;
        return dist;

sol = Solution();
print(format(5, "b"));
print(sol.binaryGap(5));
