/*
要求：O(n)时间，O(1)空间
思路：回文列表具有对称的特性，即前半段正序链表与后半段逆序链表相等。
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        #找到链表的中间结点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #对链表的后半部分进行逆转操作
        Node = None
        while slow:
            nxt = slow.next
            slow.next = Node
            Node = slow
            slow = nxt
        
        #判断前半部分与后半部分是否相等
        while Node and head:
            if Node.val != head.val:
                return False
            Node = Node.next
            head = head.next
        return True
