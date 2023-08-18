#  https://leetcode.com/problems/repeated-dna-sequences/description/
# 23:12
# 23:20
# 00:08

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen = set()
        ret = set()
        for i in range(len(s) - 9):
            setString = s[i:i+10]
            if(setString in seen):
                ret.add(setString)
            else:
                seen.add(setString)
        return list(ret)