class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:return 1
        add_a=a
        aSize=len(a)
        xd=int(len(b)/len(a))
        for i in range(xd+1):
            a+=add_a 
            print(a)
            if b in a:
                return int(len(a)/aSize)
        return -1