/*
思路：罗马字转阿拉伯数字。表示数的基本方法：除I、X、C位于大数后作为加数，位于大数前作为减数外，一般把若干罗马基本数字写在一起，它表示的数字等于各个数字的
和。七个基本数字 I ：1 V：5 X：10 L：50 C ：100 D：500 M：1000
*/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        define_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
        for i in range(len(s)):
            if i==0 or define_dict[s[i]]<=define_dict[s[i-1]]:
                res+=define_dict[s[i]]
            else:
                res+=define_dict[s[i]]-2*define_dict[s[i-1]]
        return res
