class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while(s):
            x = s.replace('()', '').replace('{}',"").replace('[]', "")
            if(len(s) == len(x) and len(x) != 0):
                return False
            s = x
        return s == ""