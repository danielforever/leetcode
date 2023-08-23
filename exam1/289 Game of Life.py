class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Any live cell with fewer than two live neighbors dies as if caused by under-population. 1 => float("-inf") => 0
        # Any live cell with two or three live neighbors lives on to the next generation. 1 => 1
        # Any live cell with more than three live neighbors dies, as if by over-population. 1 => float("-inf") => 0

        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 0 => float("inf") => 1
        def checkValid(x,y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])
        dirs = [[-1,1], [-1,0], [-1,-1], [0,1], [0,-1], [1,1], [1,0], [1,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for x,y in dirs:
                    if(checkValid(i + x, j + y)):
                        if (board[i + x][j + y] == 1 or board[i + x][j + y] == float("-inf")):
                            print("board",i + x,j + y)
                            count += 1
                if(board[i][j]):
                    if(count > 3 or count < 2):
                        board[i][j] = float("-inf")
                else:
                    if(count == 3):
                        board[i][j] = float("inf")
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == float("inf")):
                    board[i][j] = 1
                if(board[i][j] == float("-inf")):
                    board[i][j] = 0



