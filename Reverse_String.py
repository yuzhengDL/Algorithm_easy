/*
思路：相当于对字符串做轴对称变换，即设置一前一后两个指针，交换当前指针指向的数据即可。
*/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        res = list(s)
        i = 0
        j = len(res) - 1
        while i < j:
            res[j], res[i] = res[i], res[j]
            i += 1
            j -= 1
        return ''.join(res)

/*python中的简洁实现
class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
