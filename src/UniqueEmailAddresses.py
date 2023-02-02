from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailMap = {}
        count = 0
        for email in emails:
            splitEmail = email.split('@')
            if splitEmail[1] not in emailMap.keys():
                emailMap[splitEmail[1]] = list();
            localName = splitEmail[0].split('+')[0]
            localName = localName.replace('.','')
            if localName not in emailMap[splitEmail[1]]:
                emailMap[splitEmail[1]].append(localName)
                count += 1

        return count

sol = Solution()
print(sol.numUniqueEmails(["test.email+alex@leetcode.com",
                           "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
#print(sol.numUniqueEmails())
#print(sol.numUniqueEmails())