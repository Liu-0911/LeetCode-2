# 给你一个大小为 m x n 的二进制矩阵 grid 。 
# 
#  岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都
# 被 0（代表水）包围着。 
# 
#  岛屿的面积是岛上值为 1 的单元格的数目。 
# 
#  计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。 
# 
#  
# 
#  示例 1： 
#  
#  
# 输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,
# 0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,
# 0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] 为 0 或 1 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 919 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if not grid: return 0  # 为空，结束
        # row = len(grid)
        # col = len(grid[0])
        # # print(row,col)
        #
        # f = {}  # 定义 "节点 -> 父亲" 的字典
        # rank = [ 1 if grid[i][j] == 1 else 0  for i in range(row) for j in range(col) ]  # 记录集合的秩
        #
        # def find(x):
        #     f.setdefault(x,x)  # 如果在字典中x不存在，则x自身就是父亲，否则跳过
        #     if f[x] != x:  # 递归查找父亲，并给每一个节点设置的都是父亲的值，这里有路径压缩
        #         f[x] = find(f[x])
        #     return f[x]
        #
        # def union(x, y):  # 合并两个节点的父亲，并把x的父亲改为y的父亲，即将x合并到y的父亲上去，此处没有按秩合并
        #     # nonlocal maxgrid
        #     rootx = find(x)
        #     rooty = find(y)
        #     if rootx > rooty:
        #         f[rooty] = rootx
        #         rank[rootx] += rank[rooty]
        #         # maxgrid = max(maxgrid,rank[rootx])
        #
        #     elif rootx < rooty:
        #         f[rootx] = rooty
        #         rank[rooty] += rank[rootx]
        #         # maxgrid = max(maxgrid, rank[rooty])
        #
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == 1:  # 如果grid[i][j]为岛屿
        #             for x, y in [[1, 0], [0, 1]]:  # 尝试扫描该岛的 左/上边
        #                 tmp_i = i + x
        #                 tmp_j = j + y
        #                 if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == 1:  # 判断数组是否溢出，并判断 左/上是否为岛屿
        #                     union(tmp_i * col + tmp_j, i * col + j)  # 符合if条件，两点联合
        # # print(f)
        # # res = set()  # 定义结果集合，方便去重
        # # for i in range(row):  # 再次遍历
        # #     for j in range(col):
        # #         if grid[i][j] == "1":
        # #             res.add(find((i * row + j)))  # 添加父节点到集合中，即使会存在重复的父节点。
        # # print(rank)
        # maxgrid = max(rank)
        # return maxgrid # 返回集合里父节点的数量，即岛屿的个数

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
            grid[i][j] = 0
            area = 1
            while queue:
                i,j = queue.pop()
                for x,y in directions:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j]:
                        grid[tmp_i][tmp_j] = 0
                        area += 1
                        queue.appendleft((tmp_i,tmp_j))
            return area

        def dfs(i,j):
            grid[i][j] = 0
            area = 1
            for x, y in directions:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j]:
                    area += dfs(tmp_i,tmp_j)
            return area

        for i in range(lenrow):
            for j in range(lencol):
                if grid[i][j]:
                    cnt = max(cnt,dfs(i,j))
        return cnt
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[1]]
print(s.maxAreaOfIsland(grid))
# a = 10
# def changa():
#     global a
#     a = min(a,5)
# changa()
# print(a)