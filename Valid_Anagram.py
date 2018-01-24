/*
思路：通过字典统计两个字符串中各个字符出现的频率，最后通过比较字典是否相等得出结果。
*/

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return Counter(s) == Counter(t)
        
/*
思路：先排序，后比较。
*/
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return return sorted(s) == sorted(t)
