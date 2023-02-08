# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  每个右括号都有一个对应的相同类型的左括号。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "()[]{}"
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(]"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由括号 '()[]{}' 组成 
#  
# 
#  Related Topics 栈 字符串 👍 3718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        # while '()' in s or '[]' in s or '{}' in s:
        #     s = s.replace('[]', '').replace('()', '').replace('{}', '')
        # return s == ''
        # dic = {'{':'}','[': ']', '(': ')', '#': '#'}
        # stack = ['#']
        # for c in s:
        #     if c in dic:
        #         stack.append(c)
        #     elif dic[stack.pop()] != c :
        #         return False
        # return  len(stack) == 1
        if len(s) % 2:
            return False
        dic = {'{': '}', '[': ']', '(': ')', '#': '#'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif len(stack) == 0 or stack[-1] != c:
                return False
            else:
                stack.pop()
        return not stack

# leetcode submit region end(Prohibit modification and deletion)
a = 0
b = 1
if a or