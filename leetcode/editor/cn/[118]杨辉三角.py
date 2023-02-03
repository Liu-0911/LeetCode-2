# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: numRows = 1
# 输出: [[1]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics 数组 动态规划 👍 904 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0: return []
        res = [[1]]
        while len(res) < numRows:
            # print(list(zip([0]+res[-1], res[-1]+[0])))
            # print([0]+res[-1], res[-1]+[0])
            print(res[-1], res[-1])
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
print(s.generate(5))