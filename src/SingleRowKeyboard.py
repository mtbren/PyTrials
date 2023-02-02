class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        alphmap = {}
        for ind, c in enumerate(keyboard):
            alphmap[c] = ind;
        #print(alphmap)
        initPos = 0
        totalMove = 0
        prevPos = initPos
        for ind, c in enumerate(word):
            totalMove += abs(alphmap[c] - prevPos)
            prevPos = alphmap[c]
        return totalMove

sol = Solution()
print(sol.calculateTime('abcdefghijklmnopqrstuvwxyz', 'cba'))
print(sol.calculateTime('pqrstuvwxyzabcdefghijklmno', 'leetcode'))