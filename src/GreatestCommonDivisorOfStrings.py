class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1);
        len2 = len(str2);
        if len1 < len2:
            return self.gcdOfStrings1(str2, str1);
        elif len2 < len1:
            return self.gcdOfStrings1(str1, str2);
        else:
            if str1 == str2:
                return str1;
            else:
                return "";

    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        # str2 is shorter in length
        interStr = str2;
        count = 1;
        while len(interStr) > 0:
            origInterStr1 = interStr;

            while len(interStr) <= len(str1):
                if str1.count(interStr) == 0:
                    break;
                if interStr == str1:
                    return origInterStr1;
                else:
                    interStr += origInterStr1;

            interStr = str2[0: len(origInterStr1)//2];
            count = count*2;
            while str2.count(interStr) != count:
                interStr = str2[0: len(interStr) // 2];
                count = count * 2;
                if interStr=="":
                    return "";

        return "";


sol = Solution();
'''print(sol.gcdOfStrings("ABABABAB", "AB"));
print(sol.gcdOfStrings("ABABABAB", "ABC"));
print(sol.gcdOfStrings("ABCABCAB", "ABC"));
print(sol.gcdOfStrings("ABABABAB", "ABAB"));
print(sol.gcdOfStrings("ABABAB", "ABAB"));
print(sol.gcdOfStrings("LEET", "CODE"));'''
print(sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"));


'''stro = "ABC"
print(3//2);
print(stro[0:len(stro)//2]);'''