/*
法1：现将两个数组排序，再通过两个指针分别扫描两个数组，寻找共同元素
法2：调用collection模块的Counter计数器
*/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1)==0 or len(nums2)==0:
            return []
        
        
        res = []
        i = 0
        j = 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
            else:
                i = i + 1
        return res
