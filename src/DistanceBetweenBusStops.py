from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockWiseDistance = 0
        antiClockWiseDistance = 0
        if start > destination:
            temp = start
            start = destination
            destination = temp

        for i in range (start, destination):
            clockWiseDistance += distance[i]

        while(start != destination):
            if start == 0:
                start = len(distance) - 1
            else:
                start -= 1
            antiClockWiseDistance += distance[start]

        if clockWiseDistance < antiClockWiseDistance:
            return clockWiseDistance
        else:
            return antiClockWiseDistance

sol = Solution()
print(sol.distanceBetweenBusStops([1,2,3,4],0,1)) #1
print(sol.distanceBetweenBusStops([1,2,3,4],0,2)) #3
print(sol.distanceBetweenBusStops([1,2,3,4],0,3)) #4
