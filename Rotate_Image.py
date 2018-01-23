/*
 * clockwise rotate
 * first tranpose, then reverse 
 * 1 2 3     1 4 7     7 4 1
 * 4 5 6  => 2 5 8  => 8 5 2
 * 7 8 9     3 6 9     9 6 3
*/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i].reverse()
