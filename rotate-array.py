My submission:
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        
        if k == 0:
            return
        
        nums.reverse()
        start = 0
        end = k - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
        
        start = k
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1
