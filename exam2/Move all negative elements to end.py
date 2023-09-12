#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        count = 0
        ret = [0] * n
        for i in range(len(arr)):
            if(arr[i] >= 0):
                count += 1
        leftPointer = 0
        rightPointer = count
        for i in range(len(arr)):
            if(arr[i] >= 0):
                ret[leftPointer] = arr[i]
                leftPointer += 1
            else:
                ret[rightPointer] = arr[i]
                rightPointer += 1
        for i in range(len(arr)):
            arr[i] = ret[i]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends