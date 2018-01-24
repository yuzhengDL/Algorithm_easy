/*
思路：利用collections中的Counter计数器对字符串s中各个字符的出现次数进行统计；其次遍历整个字符串，找到第一个出现次数为1的字符，返回其下标。
*/

from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        od = Counter(s)
    
        for i,ss in enumerate(s):
            if od[ss] == 1:
                return i
        return -1


/*
改进：利用python中特有的count()方法统计字符串里某个字符的出现次数
*/
def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
        
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1
