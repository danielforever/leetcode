#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        PointerA,PointerB,PointerC = 0, 0, 0
        ret = []
        
        while (PointerA< n1 and PointerB < n2 and PointerC < n3):
            if (A[PointerA] == B[PointerB] and B[PointerB] == C[PointerC]):
                if(A[PointerA] not in ret):
                    ret.append(A[PointerA]) 
                PointerA += 1
                PointerB += 1
                PointerC += 1
     
            elif A[PointerA] < B[PointerB]:
                PointerA += 1
     
            elif B[PointerB] < C[PointerC]:
                PointerB += 1
     
            else:
                PointerC += 1
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends