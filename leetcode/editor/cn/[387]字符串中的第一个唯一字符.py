# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s = "leetcode"
# 输出: 0
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "loveleetcode"
# 输出: 2
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "aabb"
# 输出: -1
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 只包含小写字母 
#  
# 
#  Related Topics 队列 哈希表 字符串 计数 👍 635 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import string
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 遍历26个英文字母，而不是字符串
        # min_index = len(s)
        # for c in string.ascii_lowercase:
        #     i = s.find(c)
        #     if i != -1  and i == s.rfind(c):
        #         min_index = min(min_index,i)
        # return min_index if min_index != len(s) else -1
        # for c in s:
        #     if s.find(c) == s.rfind(c):
        #         return s.find(c)
        # return -1

        # 使用数组模拟hashtable
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] += 1
        for idx,char in enumerate(s):
            if arr[ord(char) - 97] == 1:
                return idx
        return -1

# leetcode submit region end(Prohibit modification and deletion)
# 使用数组模拟hashtable
print(ord('a'))
