/*
思路：假设f(k)代表抢k个房子所能获得的最大收益，约束条件是目标房子之间不能相邻。若我们将第k个房子作为目标，考虑到约束条件，第k-1个房子势必不能抢，因此
f(k)=vk+f(k-2)，其中vk代表第k个房子的收益；若我们不将第k个房子作为目标，则f(k)=f(k-1)，因此f(k)=max(vk+f(k-2), f(k-1))。通过动态规划算法求解即可。
*/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        a = 0
        b = nums[0]
        for i in range(1, len(nums)):
            a, b = b, max(nums[i]+a,b)
        return b
