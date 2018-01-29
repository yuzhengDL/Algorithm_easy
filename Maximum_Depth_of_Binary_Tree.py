/*
思路1：深度优先搜索。针对一个结点，递归地找到其左子树和右子树的最大深度即可
*/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        
        return (1+max(self.maxDepth(root.left), self.maxDepth(root.right)))
