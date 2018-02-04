/*
思路：堆栈
*/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dic={')':'(', ']':'[', '}':'{'}
        right = [')',']','}']
        res = []
        for bracket in s:
            if bracket in right and res==[]:
                return False
            elif bracket in right and res!=[]:
                if dic[bracket] == res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(bracket)
        return res==[]
