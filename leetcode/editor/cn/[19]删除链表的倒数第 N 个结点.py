# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1], n = 1
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2], n = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
# 
#  Related Topics 链表 双指针 👍 2385 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 加入头节点，防止最后结果链表长度小于3
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        # 需要在判断是加上fast 防止最后一个结点没有.next属性
        while fast.next:
            fast = fast.next
            slow = slow.next
        print(fast)
        slow.next = slow.next.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
