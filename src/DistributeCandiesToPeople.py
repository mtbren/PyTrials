from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        list = [];
        n = 1;
        remaining = candies;
        i = 0;
        while True:
            if (n > num_people):
                if (remaining >= n):
                    list[i] = list[i] + n;
                    remaining = remaining - n;
                else:
                    list[i] = list[i] + remaining;
                    remaining = remaining - remaining;
            else:
                if (remaining >= n):
                    list.append(n);
                    remaining = remaining - n;
                else:
                    list.append(remaining);
                    remaining = remaining - remaining;

            if remaining <= 0:
                break;
            n += 1;

            if (i == num_people - 1):
                i = 0;
            else:
                i += 1;

        while (len(list) < num_people):
            list.append(0);
        return list;


sol = Solution();
print(sol.distributeCandies(7, 4));
print(sol.distributeCandies(10, 3));
