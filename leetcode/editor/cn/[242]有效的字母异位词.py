# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "rat", t = "car"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s 和 t 仅包含小写字母 
#  
# 
#  
# 
#  进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
# 
#  Related Topics 哈希表 字符串 排序 👍 724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #   使用Counter
        # a = Counter(s)
        # b = Counter(t)
        # return a == b

        #   使用set
        # set_s = set(s)
        # set_t = set(t)
        # set_ran = set_s if len(set_s) > len(set_t) else set_t
        # for i in set_ran:
        #     if s.count(i) != t.count(i):
        #         return False
        # return True

        # 使用数组计数
        import numpy as np
        arr = np.zeros(26)
        for c in s:
            arr[ord(c) - 97] += 1
        for c in t:
            if arr[ord(c) - 97] >0:
                arr[ord(c) - 97] -= 1
            else:
                return False
        if np.sum(arr) != 0:
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
