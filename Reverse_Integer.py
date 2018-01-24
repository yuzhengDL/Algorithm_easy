/*
思路：int->str，使用str[::-1]反转，再int(str)转换成int。最后需要进行边界判断：反转后整数的绝对值不能超过2^31，并且判断是否需要加上负号。
*/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(abs(x))[::-1])
        
        if res >= 2**31:
            return 0
        
        if x < 0:
            res *= -1
        
        return res
