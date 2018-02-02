/*
思路：先求x和y的异或，再计算其中1的个数。
tips:bin()函数可以用于返回一个整数 int 或者长整数 long int 的二进制表示。
*/
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        a = x^y
        while a!=0:
            res+=1
            a&=a-1
        return res
