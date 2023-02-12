# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和
#  targetSum 。如果存在，返回 true ；否则，返回 false 。 
# 
#  叶子节点 是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
#  
# 
#  示例 2： 
#  
#  
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 解释：树中存在两条根节点到叶子节点的路径：
# (1 --> 2): 和为 3
# (1 --> 3): 和为 4
# 不存在 sum = 5 的根节点到叶子节点的路径。 
# 
#  示例 3： 
# 
#  
# 输入：root = [], targetSum = 0
# 输出：false
# 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [0, 5000] 内 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1106 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from  collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        if not root:    return False
        # if not root.left and not root.right:
        #     return sum == root.val
        # return self.hasPathSum(root.left,sum - root.val) or self.hasPathSum(root.right,sum - root.val)

        # que = deque()
        # que.append((root,root.val))
        # while que:
        #     cur,csum = que.popleft()
        #     if not (cur.left or cur.right) and sum == csum:
        #         return True
        #     if cur.left:
        #         que.append((cur.left,csum + cur.left.val))
        #     if cur.right:
        #         que.append((cur.right,csum + cur.right.val))
        # return False

        def dfs(root,csum):
            if not root:
                return False
            if not (root.right or root.left) and csum == sum:
                return True
            leftFlag,rightFlag = False,False
            if root.left:
                leftFlag = dfs(root.left,csum + root.left.val)
            if root.right:
                rightFlag = dfs(root.right,csum + root.right.val)
            return  leftFlag or rightFlag
        return dfs(root,root.val)

# leetcode submit region end(Prohibit modification and deletion)
