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
        
class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
