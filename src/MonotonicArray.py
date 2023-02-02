class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False;
        isDecreasing = False;
        isConstant = False;
        for numIdx, numVal in enumerate(nums) :
            if numIdx > 0:
                if nums[numIdx-1] < nums [numIdx]:
                    isIncreasing = True;
                if nums[numIdx-1] > nums [numIdx]:
                    isDecreasing = True;
                if nums[numIdx-1] == nums [numIdx]:
                    isConstant = True;

                if isIncreasing and isDecreasing:
                    return False;

        return True;
