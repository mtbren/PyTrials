from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        refCoordinate0 = coordinates[0]
        refCoordinate1 = coordinates[1]
        if refCoordinate1[0] - refCoordinate0[0] == 0:
            refSlope = 1
        else:
            refSlope = (refCoordinate1[1] - refCoordinate0[1]) / (refCoordinate1[0] - refCoordinate0[0])

        if len(coordinates) < 3:
            return True

        for i in range(2, len(coordinates)):
            if coordinates[i][0] - refCoordinate0[0] == 0:
                currSlope0 = 1
            else:
                currSlope0 = (coordinates[i][1] - refCoordinate0[1]) / (coordinates[i][0] - refCoordinate0[0])
            if coordinates[i][0] - refCoordinate1[0] == 0:
                currSlope1 = 1
            else:
                currSlope1 = (coordinates[i][1] - refCoordinate1[1]) / (coordinates[i][0] - refCoordinate1[0])

            if currSlope1 != refSlope or currSlope0 != refSlope:
                return False

        return True


sol = Solution()
print(sol.checkStraightLine([[1,2],[1,3],[1,4],[1,5],[1,6],[6,7]]))
print(sol.checkStraightLine([[0,0],[0,1],[0,-1]]))
print(sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
