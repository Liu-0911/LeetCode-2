# 给你一个二叉树的根节点 root ， 检查它是否轴对称。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 1000] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你可以运用递归和迭代两种方法解决这个问题吗？ 
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 2267 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True

        # def compare(left,right):
        #     #   如果左右节点都空
        #     if not (left or right):
        #         return True
        #     #   如果左右节点有一个空
        #     if not (left and right):
        #         return False
        #     #   如果左右节点都非空但值不相等
        #     if left.val != right.val:
        #         return False
        #     return compare(left.left, right.right) and compare(left.right, right.left)
        #
        # return compare(root.left,root.right)

        que = deque()
        que.append(root.left)
        que.append(root.right)

        while que:
            leftnode = que.popleft()
            rightnode = que.popleft()
            if not (leftnode or rightnode):
                continue
            if not (leftnode and rightnode):
                return False
            if leftnode .val != rightnode.val:
                return False
            que.append(leftnode.left)
            que.append(rightnode.right)
            que.append(leftnode.right)
            que.append(rightnode.left)
        return True

# leetcode submit region end(Prohibit modification and deletion)
