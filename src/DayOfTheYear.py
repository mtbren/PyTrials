class Solution:
    def dayOfYear(self, date: str) -> int:
        monthDays = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        givenMonth = int(date[5:7])
        givenDate = int(date[8:])
        givenYear = int(date[:4])

        totalDays = givenDate
        for m in range(1, givenMonth):
            totalDays += monthDays[m]

        if givenMonth > 2:
            if givenYear % 4 == 0:
                totalDays += 1

            if givenYear % 100 == 0:
                if givenYear % 400 != 0:
                    totalDays -= 1

        return totalDays


sol = Solution()
#print(sol.dayOfYear('2022-03-10'))
print(sol.dayOfYear('2004-03-01'))