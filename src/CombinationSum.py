from typing import List


class CombinationSum:
    retList: List[List[int]];
    def getCombinationSums(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates);
        if(target in candidates):
            self.retList.append([target]);

        iPtr = 0;
        while True:
            self.getDistinctCombinationSums()
        return myList;

    def getDistinctCombinationSums(self, candidates: List[int], target: int, addendum: List[int]):
        sum = 0;
        for val in addendum:
            sum = sum + val ;

        if target - sum in candidates:
            self.retList.append(addendum.append(target-sum));
        return None;
sol = CombinationSum();
print(sol.getCombinationSums([2,3,6,7],7));