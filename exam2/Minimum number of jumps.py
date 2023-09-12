#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
        dp = [0] + [float('inf')] * (n - 1)
        for i in range(n):
            for j in range(1, arr[i] + 1):
                if(i + j < n):
                    if (dp[i] + 1 < dp[i + j]):
                        dp[i + j] = dp[i] + 1
        if (dp[-1] == float("inf")): return -1
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends