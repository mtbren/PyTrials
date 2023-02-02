from typing import List


class Solution:
    retList = list(list());
    allKLists = list(list());

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.retList = [];
        #self.combination3(k, [], n);
        self.getAllCombinations(k, [], n);
        return self.allKLists;

    def getAllCombinations(self, k: int, kList: List[int], n):
        if len(kList) < k:
            for i in range(1,10):
                kList.append(i);
                self.getAllCombinations(k,kList, n);
        elif len(kList) == k:
            self.allKLists.append(kList.copy());
        elif len(kList) > 0:
            kList.pop();


    def combination3(self, k: int, kList: List[int], n):

        if len(kList) == k:
            sum = 0;
            for val in kList:
                sum += val;
            if sum == n:
                if (len(set(kList)) == len(kList)):
                    if sorted(kList) not in self.retList:
                        self.retList.append(sorted(kList.copy()));
            # kList.pop();
        elif len(kList) < k:
            for i in range(1, 10):
                if i in kList:
                    continue;

                kList.append(i);
                self.combination3(k, kList, n);
                if len(kList) > 0:
                    if i == 9 or len(kList) == k:
                        kList.pop();


sol = Solution();
# print(sol.combinationSum3(3, 7));
print(sol.combinationSum3(2, 4));
#print(sol.combinationSum3(3, 9));
# print(sol.combinationSum3(9, 45));
# print(sol.combinationSum3(4, 24));
