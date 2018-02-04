/*
思路1：先排序，再遍历排序好的数组找出丢失的数字
*/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return i+1

/*
思路2：先利用求和公式sum=(1+n)*n/2对0,1,2,...,n求和，在求出当前数组的和，两者相减即为丢失的数字。
*/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return (1+len(nums))*len(nums)/2-sum(nums)
