/*
思路1：迭代。广度优先搜索，不断比较左孩子的左结点和右孩子的右结点以及左孩子的右结点和右孩子的左结点取值是否相等。需要构建一个队列。
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
    

/*
思路2：递归。
Two trees are a mirror reflection of each other if:
1.Their two roots have the same value.
2.The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
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

        return self.isSym(root.left, root.right)
    
    def isSym(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val == right.val:
            return self.isSym(left.left,right.right) and self.isSym(left.right, right.left)        
        else:
            return False
