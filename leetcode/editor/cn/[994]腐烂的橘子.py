# 在给定的 m x n 网格
#  grid 中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。 
# 
#  返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
# 
#  Related Topics 广度优先搜索 数组 矩阵 👍 654 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        que = deque()
        # print(np.mat(mat))

        m = len(grid)
        n = len(grid[0])
        time = 0
        numof1 = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j,time))
                elif grid[i][j] == 1:
                    numof1 += 1

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while que:
            x, y, time = que.popleft()
            for dx, dy in directions:
                newx = dx + x
                newy = dy + y
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] == 1:
                    numof1 -= 1
                    grid[newx][newy] = 2
                    que.append((newx, newy,time + 1))
        if numof1:
            return -1
        return time

# leetcode submit region end(Prohibit modification and deletion)
a = {123}
b = {123, 345}
print(b - a)
if not a:
    print("空了")
elif a:
    print("没空")