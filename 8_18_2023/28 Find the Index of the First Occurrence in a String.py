class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(haystack) == 1):
            if haystack == needle:
                return 0
        for i in range(len(haystack)-(len(needle) - 1)):
            print(haystack[i:i+len(needle)])
            if(haystack[i:i+len(needle)] == needle):
                return i
        return -1
