/*
思想：现将list中的各位数字转化成整数，然后进行加一操作，最后再转换成list。
*/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        a = 0
        res = []
        length = len(digits)
        for (i,digit) in enumerate(digits):
            a += digit*10**(length-i-1)
        
        a += 1
        while a!=0:
            res.append(a%10)
            a //= 10
        res.reverse()
        return res
