# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。 
# 
#  两个相邻元素间的距离为 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 10⁴ 
#  1 <= m * n <= 10⁴ 
#  mat[i][j] is either 0 or 1. 
#  mat 中至少有一个 0 
#  
# 
#  Related Topics 广度优先搜索 数组 动态规划 矩阵 👍 808 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
import numpy as np
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        que = deque()
        # print(np.mat(mat))

        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                # 用-1来标记当前的1没有访问过 如果不是1则存放了最短距离
                if mat[i][j] == 1:
                    mat[i][j] = -1
                elif mat[i][j] == 0:
                    que.append((i, j))

        # print(np.matrix(mat))
        # print(que)

        # while que:
        #     x, y, val = que.popleft()
        #     if x > 0 and mat[x - 1][y] == -1:
        #         mat[x - 1][y] = val + 1
        #         que.append((x - 1, y, val + 1))
        #     if y > 0 and mat[x][y - 1] == -1:
        #         mat[x][y - 1] = val + 1
        #         que.append((x, y - 1, val + 1))
        #     if x < m - 1 and mat[x + 1][y] == -1:
        #         mat[x + 1][y] = val + 1
        #         que.append((x + 1, y, val + 1))
        #     if y < n - 1 and mat[x][y + 1] == -1:
        #         mat[x][y + 1] = val + 1
        #         que.append((x, y + 1, val + 1))
        #     print(np.matrix(mat))
        #     print(que)

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while que:
            x, y = que.popleft()
            for dx, dy in directions:
                newx = dx + x
                newy = dy + y
                if 0 <= newx < m and 0 <= newy < n and mat[newx][newy] == -1:
                    mat[newx][newy] = mat[x][y] + 1
                    que.append((newx,newy))
            # print(np.matrix(mat))
            # print(que)
        return mat
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# mat = [[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
s.updateMatrix(mat)

print(np.matrix(mat))