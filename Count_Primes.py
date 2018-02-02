/*
思路：埃拉托斯特尼筛法。给出要筛数值的范围n，找出以内的素数。先用2去筛，即把2留下，把2的倍数剔除掉；再用下一个质数，也就是3筛，把3留下，把3的倍数剔除掉；
接下去用下一个质数5筛，把5留下，把5的倍数剔除掉；不断重复下去......。
*/

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        isPrimes = [True] * n
        isPrimes[0] = isPrimes[1] = False
        for i in range(2, int(n**0.5)+1):
            if isPrimes[i]==True:
                isPrimes[i*i:n:i] = [False] * len(isPrimes[i*i:n:i])
        return sum(isPrimes)
