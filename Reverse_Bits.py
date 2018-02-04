/*
思路：按位操作。按位从低位逐一取出原数字的二进制位，然后逆序排列。
*/
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res <<= 1
            res |= (n>>i &1)
        return res
