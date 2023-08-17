# https://leetcode.com/problems/set-matrix-zeroes/description/
# 20:24
# 20:31
# 00:07
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    x = 0
                    y = 0
                    while(x < len(matrix)):
                        if(x != i and matrix[x][j] != 0):
                            matrix[x][j] = float('-inf') 
                        x += 1
                    while(y < len(matrix[0])):
                        if(y != j and matrix[i][y] != 0):
                            matrix[i][y] = float('-inf') 
                        y += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('-inf'):
                    matrix[i][j] = 0