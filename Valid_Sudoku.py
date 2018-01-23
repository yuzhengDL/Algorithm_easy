/*
参考博客https://www.cnblogs.com/breada/p/4924092.html
数独规则：1.任意行只包含1-9不重复的数字；2.任意列只包含1-9不重复的数字；3.任意宫（3X3）只包含1-9不重复的数字
一些注意事项：
1.遍历得到list，使用列表解析式 unit = [i for i in s if i != '.']
2.减少变量的使用
3.zip变量
4.对列表的操作，可以减少append等操作，选择+
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
