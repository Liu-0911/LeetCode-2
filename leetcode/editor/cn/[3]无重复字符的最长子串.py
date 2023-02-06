# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
# 
#  Related Topics 哈希表 字符串 滑动窗口 👍 8678 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np
'''
用双指针维护一个滑动窗口去裁减字符串子串
建立一个哈希表来跟踪重复字符的最新位置
不断移动右指针，每当遇到一个重复字符c时，在确保左指针不往反方向移动时将其移到c的下一位
移动右指针的过程中，不断维护一个最大长度值并在程序末尾处返回
'''
class Solution:
    def lengthOfLongestSubstring(self,s):
        # 特解
        if len(s) <= 1:
            return len(s)

        # 初始化左指针, 子串最大长度
        left, max_len = 0, 0

        # 创立哈希表用来跟踪每一个重复字符的位置
        # 当右指针碰到了表中的某一个重复字符c, 在确保左指针不往反方向移动时跳到s的下一位
        hashtable = {}

        # 不断移动右指针
        for right in range(len(s)):
            # cur_char表示当前字符
            cur_char = s[right]
            # 如果当前字符之前重复过(重复位置为hashtable[cur_char])
            if cur_char in hashtable:
                # 在确保左指针不往反方向移动时将左指针移到重复位置 + 1
                if hashtable[cur_char] + 1 >= left:
                    left = hashtable[cur_char] + 1
            # 更新当前字符最新重复位置为当前右指针位置
            hashtable[cur_char] = right
            # 在移动右指针的过程中，不断维护一个最大长度值
            max_len = max(max_len, right - left + 1)
        # 返回最大长度
        return max_len
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
s1 = 'abba'
print(s.lengthOfLongestSubstring(s1))