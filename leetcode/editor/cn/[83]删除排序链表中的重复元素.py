# 给定一个已排序的链表的头
#  head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：head = [1,1,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
#  
#  
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围 [0, 300] 内 
#  -100 <= Node.val <= 100 
#  题目数据保证链表已经按升序 排列 
#  
# 
#  Related Topics 链表 👍 934 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #   递归
        # if not head or not head.next:
        #     return head
        # head.next = self.deleteDuplicates(head.next)
        # return head if head.val !=  head.next.val else head.next

        #   遍历
        if not head or not head.next:
            return head
        pre,curr = head,head.next
        while curr:
            if curr.val == pre.val:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        return head

# leetcode submit region end(Prohibit modification and deletion)
