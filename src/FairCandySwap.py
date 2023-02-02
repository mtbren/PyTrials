from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes = sorted(aliceSizes);
        bobSizes = sorted(bobSizes);
        aliceSum = 0 ;
        bobSum = 0 ;
        for size in aliceSizes :
            aliceSum += size ;
        for size in bobSizes :
            bobSum += size ;
        total = aliceSum + bobSum ;
        aliceNeeds = (total/2)-aliceSum;
        bobNeeds = (total/2)-bobSum;
        retList = [];
        bobPtr = 0;
        alicePtr = 0;

        #print(targetDiff);
        while 1:
            diff = bobSizes [bobPtr] - aliceSizes[alicePtr];
            if(diff==aliceNeeds):
                retList.append(aliceSizes[alicePtr]);
                retList.append(bobSizes[bobPtr]);
                break;
            elif(diff>aliceNeeds):
                alicePtr+=1;
            elif(diff<aliceNeeds):
                bobPtr+=1;

            if(alicePtr >= len(aliceSizes)):
                break;
            if (bobPtr >= len(bobSizes)):
                break;

        return retList;



sol = Solution();
print(sol.fairCandySwap([1,2],[2,3]));
print(sol.fairCandySwap([23,44,34,42,53,12,76,64,76,45],[18,75,88,90,73,13,30,70,5,29]));
print(sol.fairCandySwap([2],[1,3]));