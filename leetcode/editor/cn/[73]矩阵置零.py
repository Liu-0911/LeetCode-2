# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#  
# 
#  示例 2： 
#  
#  
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[0].length 
#  1 <= m, n <= 200 
#  -2³¹ <= matrix[i][j] <= 2³¹ - 1 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  一个直观的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。 
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。 
#  你能想出一个仅使用常量空间的解决方案吗？ 
#  
# 
#  Related Topics 数组 哈希表 矩阵 👍 828 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ####################### 复杂度为O(M+N) ############################
        lenrow = len(matrix)
        lencol = len(matrix[0])
        row_zero = set()
        col_zero = set()
        for i in range(lenrow):
            for j in range(lencol):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(lenrow):
            for j in range(lencol):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
        ####################### 复杂度为O(1) ############################
        # flag_row0 = False
        # flag_col0 = False
        # lenrow = len(matrix)
        # lencol = len(matrix[0])
        # # 判断第一列是否有零
        # for j in range(lenrow):
        #     if matrix[j][0] == 0:
        #         flag_col0 = True
        #         break
        # # 判断第一行是否有零
        # for i in range(lencol):
        #     if matrix[0][i] == 0:
        #         flag_row0 = True
        #         break
        # # 判断其他地区是否有零，用第一行和第一列作为标志位
        # for i in range(1, lenrow):
        #     for j in range(1, lencol):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = matrix[0][j] = 0
        # # 置0
        # for i in range(1, lenrow):
        #     for j in range(1, lencol):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0
        # if flag_row0:
        #     for i in range(lencol):
        #         matrix[0][i] = 0
        #
        # if flag_col0:
        #     for i in range(lenrow):
        #         matrix[i][0] = 0
# leetcode submit region end(Prohibit modification and deletion)
