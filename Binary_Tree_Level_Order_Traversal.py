/*
思路：广度优先遍历。分别遍历二叉树的每一层，直至该层的结点数为0
*/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        
        a = [root]
        q = [[root.val]]
        while True:
            res = []
            for i in range(len(a)):
                if a[0].left:
                    res.append(a[0].left.val)
                    a.append(a[0].left)
                if a[0].right:
                    res.append(a[0].right.val)
                    a.append(a[0].right)
                del a[0]
            if res == []:
                break
            q.append(res)
        return q
