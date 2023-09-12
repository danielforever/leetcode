#User function Template for python3
class Solution:
	def isPalindrome(self, S):
		# code here
		
		leftPointer = 0
		rightPointer = len(S) - 1
		
		while(leftPointer <= rightPointer):
		    if(S[leftPointer] != S[rightPointer]):
		        return 0
		    leftPointer += 1
		    rightPointer -= 1 
		return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends