from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scoreByID = {}
        for score in items:
            if score[0] in scoreByID.keys():
                scoreByID[score[0]].append(score[1])
            else:
                scoreByID[score[0]] = [];
                scoreByID[score[0]].append(score[1])

        highFive = []
        for id in scoreByID.keys():
            scoreByID[id] = sorted(scoreByID[id], reverse=True)
            i = 0
            avg = 0
            sum = 0
            for ind, score in enumerate(scoreByID[id]):
                sum += score
                i += 1
                if i == 5 or ind == (len(scoreByID[id]) - 1):
                    divisor = i
                    if ind == len(scoreByID[id]) - 1:
                        divisor = ind + 1
                    avg = int(sum / divisor)
                    listToAppend = list()
                    listToAppend.append(id)
                    listToAppend.append(avg)
                    highFive.append(listToAppend);
                    break

        return sorted(highFive)

sol = Solution()
print(sol.highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))
print(sol.highFive([[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]))
print(sol.highFive([[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]))