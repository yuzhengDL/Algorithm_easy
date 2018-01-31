/*
思路：二分查找算法即可
*/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return
        return self.isbad(0, n)
        
    def isbad(self, low, high):
        mid = low + (high - low) // 2
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        elif not isBadVersion(mid):
            return self.isbad(mid+1, high)
        else:
            return self.isbad(0, mid-1)
