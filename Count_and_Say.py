class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        last = "1"
        for i in range(1,n):
            res = ""
            count = 1
            pattern = last[0]
            for i in range(1,len(last)): 
                if last[i] == pattern:
                    count += 1
                else:
                    res = res + str(count) + pattern 
                    pattern = last[i]
                    count = 1
            last = res + str(count) + pattern
        return last
