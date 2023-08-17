# https://leetcode.com/problems/minimum-window-substring/description/

# 20:42
# 21:14
# 00:32
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(s) < len(t)):    return ""
        lookup = Counter(t)
        minLength = float("inf")
        output = ""
        S = len(s)
        start, end = 0, 0
        count = len(lookup)
        
        while end < S:
            
            while end < S and count != 0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -=1
                end += 1
            while start <= end and count == 0:
                
                if end-start < minLength:
                    minLength = end - start
                    output = s[start:end]
                
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]] > 0:
                        count += 1
                
                start += 1

        return output 