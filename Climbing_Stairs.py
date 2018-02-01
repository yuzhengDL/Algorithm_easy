/*
思路：每一步可以走1个或2个台阶，因此可以将该问题划分成两个子问题，即f(n)=f(n-1)+f(n-2).
*/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n==0 or n == 1:
            return 1
        
        a = b = 1
        for i in range(1, n):
            a, b = b, a+b
        return b
