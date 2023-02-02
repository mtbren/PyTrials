import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971/01/01 was a Friday
        givenDate = datetime.date(year=year, month=month, day=day)
        print(givenDate.weekday())
        firstDate = datetime.date(year=1971, month=1, day=1)
        print(firstDate.weekday())

        datetime.datetime.__add__()
        return ""


sol = Solution()
sol.dayOfTheWeek(8, 1, 2023)
