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
        # from collections import deque
        # if not grid:
        #     return 0
        # lenrow = len(grid)
        # lencol = len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # cnt = 0
        #
        # def bfs(i,j):
        #     queue = deque()
        #     queue.appendleft((i,j))
        #     grid[i][j] = '0'
        #     while queue:
        #         i,j = queue.pop()
        #         for x,y in directions:
        #             tmp_i = i + x
        #             tmp_j = j + y
        #             if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j] == '1':
        #                 grid[tmp_i][tmp_j] = '0'
        #                 queue.appendleft((tmp_i,tmp_j))
        #
        # def dfs(i,j):
        #     grid[i][j] = '0'
        #     for x, y in directions:
        #         tmp_i = i + x
        #         tmp_j = j + y
        #         if 0 <= tmp_i < lenrow and 0 <= tmp_j < lencol and grid[tmp_i][tmp_j] == '1':
        #             dfs(tmp_i,tmp_j)
        #
        # for i in range(lenrow):
        #     for j in range(lencol):
        #         if grid[i][j] == '1':
        #             dfs(i,j)
        #             cnt += 1
        # return cnt

        #   并查集
        f = {}  # 定义 "节点 -> 父亲" 的字典

        def find(x):
            f.setdefault(x,x)  # 如果在字典中x不存在，则x自身就是父亲，否则跳过
            if f[x] != x:  # 递归查找父亲，并给每一个节点设置的都是父亲的值，这里有路径压缩
                f[x] = find(f[x])
            return f[x]

        def union(x, y):  # 合并两个节点的父亲，并把x的父亲改为y的父亲，即将x合并到y的父亲上去，此处没有按秩合并
            f[find(x)] = find(y)

        if not grid: return 0  # 为空，结束
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":  # 如果grid[i][j]为岛屿
                    for x, y in [[1, 0], [0, 1]]:  # 尝试扫描该岛的 左/上边
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":  # 判断数组是否溢出，并判断 左/上是否为岛屿
                            union(tmp_i * row + tmp_j, i * row + j)  # 符合if条件，两点联合
        # print(f)
        res = set()  # 定义结果集合，方便去重
        for i in range(row):  # 再次遍历
            for j in range(col):
                if grid[i][j] == "1":
                    res.add(find((i * row + j)))  # 添加父节点到集合中，即使会存在重复的父节点。
        print(f)
        return len(res)  # 返回集合里父节点的数量，即岛屿的个数
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
grid = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"] ]
print(s.numIslands(grid))