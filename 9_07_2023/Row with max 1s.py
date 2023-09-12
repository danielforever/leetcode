#User function Template for python3
from collections import Counter

class Solution:

	def rowWithMax1s(self,arr, n, m):
	    
		# code here
		maxCount = 0
		maxRow = -1
		currRow = len(arr) - 1
		
		for row in range(len(arr)-1,-1,-1):
		    count = Counter(arr[row])
		    if( 1 in count):
		        
		        if(count[1] >= maxCount):
		            maxCount = count[1]
		            maxRow = currRow
		    currRow -= 1
		return maxRow
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends