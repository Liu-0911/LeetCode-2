# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 
# next 指针连接，'#' 标志着每一层的结束。
#  
# 
#  
#  
# 
#  示例 2: 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量在
#  [0, 2¹² - 1] 范围内 
#  -1000 <= node.val <= 1000 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 链表 二叉树 👍 939 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    from collections import deque
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # queue = deque()
        # queue.appendleft(root)
        # while queue:
        #     size = len(queue)
        #     print(size)
        #     pre = None
        #     for i in range(size):
        #         curr = queue.pop()
        #         if pre:
        #             pre.next = curr
        #         pre = curr
        #         if curr and curr.left:
        #             queue.appendleft(curr.left)
        #             queue.appendleft(curr.right)
        # return root
        if not root:
            return root
        cur = root

        while cur:
            dummy = Node()
            pre = dummy
            while(cur and cur.left):
                pre.next = cur.left
                pre = pre.next
                pre.next = cur.right
                pre = pre.next
                cur = cur.next
            cur = dummy.next
        return root

        
# leetcode submit region end(Prohibit modification and deletion)
