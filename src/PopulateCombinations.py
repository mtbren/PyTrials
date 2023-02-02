from typing import List


class CombinationsPopulator:
    finalList = list();
    threeList = list();
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.finalList=[];
        self.threeList=[];
        self.populateCombinations(k,[], 1);
        for listt in self.finalList:
            sum = 0;
            for i in listt:
                sum += i;
            if sum == n:
                self.threeList.append(listt);
        return self.threeList;

    def populateCombinations(self, k: int, kList: List[int], startFrom: int):
        if len(kList) == k:
            self.finalList.append(list(kList));
        elif len(kList) > k:
            None;
        else:
            for i in range(startFrom, 10):
                if i not in kList:
                    kList.append(i);
                    self.populateCombinations(k,kList,i+1);

        if len(kList) > 0:
            kList.pop();


    #populateCombinations();

sol=CombinationsPopulator();
sol.combinationSum3(3, 9);
print(sol.threeList);