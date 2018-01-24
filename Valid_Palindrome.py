/*
问题：判断回文数。
思路：取出字符串中的所有字符或是数字并形成一个列表，然后判断其与自身的反转列表是否相等。
关键函数：str.isalnum() 判断当前字符串是否是字母或是数字；str.isalpha() 判断当前字符串是否是字母；str.isdigit() 判断当前字符串是否是数字。
*/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        string = [i for i in s.lower() if i.isalnum()]
        return string == string[::-1]
