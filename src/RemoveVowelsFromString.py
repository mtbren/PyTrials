class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou');
        retStr = '';
        for c in s:
            if c not in vowels:
                retStr = retStr + c;
        return retStr;

sol = Solution();
print(sol.removeVowels("leetcodeisacommunityforcoders"));
print(sol.removeVowels("aeiou"));
print(sol.removeVowels("a"));
print(sol.removeVowels("abcdfghjklmnpqrstvwxyz"));
