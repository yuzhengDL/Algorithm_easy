/*
思路：求最大子段和，使用动态规划。具体分析在算法书第72页。
*/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a = 0
        res = float('-inf')
        for num in nums:
            if a > 0:
                a += num
            else:
                a = num
            if a > res:
                res = a
        return res
