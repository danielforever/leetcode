#User function Template for python3


class Solution:
    def maxArea(self,M, n, m):
        # code here
        def mah(heights):
            st=[]
            maxArea=0
            for bar in heights+[-1]:
                step=0
                while st and st[-1][1]>=bar:
                    w,h=st.pop()
                    step+=w
                    maxArea=max(maxArea,step*h)
                st.append((step+1,bar))
            return maxArea
        ans=0
        for i in range(n):
            for j in range(m):
                if i>0 and M[i][j]!=0:
                    M[i][j]=M[i-1][j]+M[i][j]
            ans=max(ans,mah(M[i]))
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends