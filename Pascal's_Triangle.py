/*
问题描述：
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
思路：
第n行由第n-1行决定，行首和行尾都是1，中间元素由第n-1行的元素两两相加得到。
*/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        
        res = [[1]]
        for i in range(1,numRows):
            a=[1]
            for j in range(i-1):
                a.append(res[i-1][j]+res[i-1][j+1])
            a.append(1)
            res.append(a)
        return res
