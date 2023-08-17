# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

# 22:10
# 22:37
# 00:27

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        leftPointer = 0
        rightPointer = 0
        count = 0
        wordDict = {}
        maxLength = 0
        while(rightPointer < len(s)):
            if(s[rightPointer] in wordDict):
                if(wordDict.get(s[rightPointer]) == 0): count += 1
                wordDict[s[rightPointer]] += 1 
            else:
                wordDict[s[rightPointer]] = 1
                count += 1 
            while(count > 2):
                wordDict[s[leftPointer]] -= 1
                if(wordDict.get(s[leftPointer]) == 0):
                    count -= 1
                leftPointer += 1 
            maxLength = max(maxLength, rightPointer - leftPointer + 1)
            rightPointer += 1    
        return maxLength    
                
