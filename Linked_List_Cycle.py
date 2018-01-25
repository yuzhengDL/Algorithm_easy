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

