from pprint import pprint
from typing import List


class ReorderDataInLogFiles:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        digitLogs = [];
        idContentDict = {};
        contentIdDict = {};
        finalList = [];
        for str in logs:
            if str[len(str) - 1] in digits:
                # print(str, " - is digit-log");
                digitLogs.append(str);
            else:
                # print(str, " - is letter-log");
                id = '';
                content = str[str.index(" ") + 1::];
                contentIdDict[content] = [];
                for innerStrInd, innerStr in enumerate(str.split(" ")):
                    # print(innerStr, " -> innerstr ||| ", innerStrInd, " -> innerstrInd");
                    if innerStrInd == 0:
                        idContentDict[innerStr] = [];
                        id = innerStr;
                        contentIdDict[content].append(id);
                    else:
                        idContentDict[id].append(innerStr);

        pprint(idContentDict);
        pprint(contentIdDict);


sol = ReorderDataInLogFiles();
sol.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]);
sol.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]);
