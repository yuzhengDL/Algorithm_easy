/*
思路：迭代，指定一前一后两个指针，通过中间变脸temp实现链表的反转。
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow = None
        while head:
            curr = head
            head = head.next
            temp = slow
            slow = curr
            curr.next = temp
        return slow


/*
思路：递归。
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
