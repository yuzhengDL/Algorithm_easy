/*
思路：设置双指针fast和slow.首先移动fast指针，使得fast指针和slow指针之间的距离相差n+1；然后同时移动fast和slow直至fast到达链表的末尾，此时slow指针指向
待删除结点的前一结点，只需修改该结点的next指向即可。
*/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        fast = slow = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
