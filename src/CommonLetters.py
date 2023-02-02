from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        swDict = {};

        shortestWord = words[0];
        for word in words:
            if len(word) < len(shortestWord):
                shortestWord = word;

        if len(words)>1:
            words.remove(shortestWord);
        else:
            return list(shortestWord);

        for letter in shortestWord:
            if letter in swDict.keys():
                swDict[letter] += 1;
            else:
                swDict[letter] = 1;

        '''print(swDict);
        print(shortestWord);'''

        retArr = [];
        for letter, times in swDict.items():
            minCount = times;
            for word in words:
                if word.count(letter) <= minCount:
                    minCount = word.count(letter);
            for i in range(0,minCount):
                retArr.append(letter);

        return retArr;

sol = Solution();

print(sol.commonChars(["dadaabaa","bdaaabcc","abccddbb","bbaacdba","ababbbab","ccddbbba","bbdabbda","bdabaacb"]));
print(sol.commonChars(["bella","label","roller"]));
print(sol.commonChars(["cool","lock","cook"]));
print(sol.commonChars(["cook"]));
