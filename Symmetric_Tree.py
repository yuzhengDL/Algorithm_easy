/*
思路1：递归。广度优先搜索，不断比较左孩子的左结点和右孩子的右结点以及左孩子的右结点和右孩子的左结点取值是否相等。需要构建一个队列。
*/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True

        stack = [[root.left, root.right]]

        while len(stack) > 0:
          pair = stack.pop(0)
          left = pair[0]
          right = pair[1]

          if left is None and right is None:
            continue
          if left is None or right is None:
            return False
          if left.val == right.val:
            stack.insert(0, [left.left, right.right])

            stack.insert(0, [left.right, right.left])
          else:
            return False
        return True
