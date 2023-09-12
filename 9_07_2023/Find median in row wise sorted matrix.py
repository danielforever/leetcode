#User function Template for python3

import heapq
from typing import List


class Node:
    def __init__(self, data: int, row: int, col: int):
        self.data = data
        self.row = row
        self.col = col
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def median(self, matrix, R, C):
    	#code here 
        minheap = []
        count = 0
        median = -1
        medianindex = (R * C) // 2
 
        for i in range(R):
            temp = Node(matrix[i][0], i, 0)
            heapq.heappush(minheap, temp)

        while count <= medianindex:
            top = heapq.heappop(minheap) 
            row = top.row
            col = top.col
            median = top.data
 
            count += 1

            if col + 1 < C:
                col += 1
                temp = Node(matrix[row][col], row, col)
                heapq.heappush(minheap, temp)
 
        return median

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends