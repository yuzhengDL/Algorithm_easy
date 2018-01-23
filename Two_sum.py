/*
思路：先将原来数组拷贝一份，然后排序；其次，使用两个指针，一个指向头，一个指向尾，两个指针向中间移动并检查两个指针指向的数的和是否为target。如果找到了这
两个数，再将这两个数在原数组中的位置找出来就可以了；最后在原数组中找下标时，需要一个从头找，一个从尾找，否则针对两个重复元素，其下标一致。
思路2：使用哈希（dict）
*/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        res = []
        numtosort = nums[:]
        numtosort.sort()      #拷贝数组并排序
        i = 0
        j = len(numtosort) - 1
        while i < j:
            if numtosort[i] + numtosort[j] == target:
                for k in range(0,len(nums)):
                    if nums[k] == numtosort[i]:
                        res.append(k)
                        break
                for k in range(len(nums)-1,-1,-1):
                    if nums[k] == numtosort[j]:
                        res.append(k)
                        break
                break
            elif numtosort[i] + numtosort[j] < target:
                i = i + 1
            else:
                j = j - 1
        return res
        
/*
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
*/
