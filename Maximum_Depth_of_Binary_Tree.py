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

    
    
    
/*
思路2：广度优先搜素。即通过队列按层次访问二叉树。
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
        
        #判断是否为空树
        if not root:
            return 0
        
        depth = 0
        q = [root]
        
        #通过列表来实现队列，即实现数据的先进先出
        while len(q)!=0:
            depth += 1
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                del q[0]
        return depth
