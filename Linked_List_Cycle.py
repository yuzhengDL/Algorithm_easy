/*
思路：快慢指针算法。慢指针一次移动一步，快指针一次移动两步。如果链表中没有循环，则快指针会比慢指针先到达链表的末尾，两者不会相遇；若链表中存在循环，快指
针最终会追上慢指针，使得fast=slow
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

/*
思路：哈希表（在python中是字典）。通过哈希表存储曾经访问过的结点，若此时存在已经被访问过的结点，则代表存在循环
注意：16个测试样例通过了13个，剩下的都超时了，说明dict在该问题中并不实用
*/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        dic = {}
        while head:
            if head not in dic.keys():
                dic[head] = 1
                head = head.next
            else:
                return True
        return False
