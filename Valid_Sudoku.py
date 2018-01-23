/*
参考博客https://www.cnblogs.com/breada/p/4924092.html.
*/


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValid(row):
                return False
        
        for col in zip(*board):
            if not self.isValid(col):
                return False
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(square):
                    return False
        
        return True
        
    def isValid(self, s):
        unit = [i for i in s if i != '.']
        return len(unit) == len(set(unit))
