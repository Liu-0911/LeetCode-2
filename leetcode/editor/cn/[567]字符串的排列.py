# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
# 
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 853 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1 = Counter(s1)
        left,right = 0,len(s1) - 1
        c2 = Counter(s2[left:right])
        while right < len(s2):
            # 把 right 位置的元素放到 counter2 中
            c2[s2[right]] += 1
            if c1 == c2:
                return True
            right += 1
            # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            c2[s2[left]] -= 1
            # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
            if c2[s2[left]] == 0:
                del c2[s2[left]]
            left += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
