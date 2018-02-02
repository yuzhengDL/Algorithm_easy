/*
思路1：按位与。
*/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            count += n & 1
            n = n>>1
        return count

/*
思路2：通过n&(n-1)操作来不断从后往前减少n中1的个数，直至n为0。
*/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n!=0:
            count += 1
            n &=n-1
        return count
