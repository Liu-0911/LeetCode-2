# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1495 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # leftdepth = self.maxDepth(root.left)
        # rightdepth = self.maxDepth(root.right)
        #
        # return max(leftdepth,rightdepth) + 1

        if not root:
            return 0
        que = [root]
        depth = 0
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            depth += 1
        return depth
# leetcode submit region end(Prohibit modification and deletion)
