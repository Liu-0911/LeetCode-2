# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 2054 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque
        if not grid:
            return 0
        lenrow = len(grid)
        lencol = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cnt = 0

        def bfs(i,j):
            queue = deque()
            queue.appendleft((i,j))
            grid[i][j] = '0'
            while queue:
                i,j = queue.pop()
                for x,y in directions:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j] == '1':
                        grid[tmp_i][tmp_j] = '0'
                        queue.appendleft((tmp_i,tmp_j))

        def dfs(i,j):
            grid[i][j] = '0'
            for x, y in directions:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j] == '1':
                    dfs(tmp_i,tmp_j)

        for i in range(lenrow):
            for j in range(lencol):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
