# 有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。 
# 
#  你也被给予三个整数 sr , sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。 
# 
#  为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对
# 应 四个方向上 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。 
# 
#  最后返回 经过上色渲染后的图像 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
#  
# 
#  示例 2: 
# 
#  
# 输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# 输出: [[2,2,2],[2,2,2]]
#  
# 
#  
# 
#  提示: 
# 
#  
#  m == image.length 
#  n == image[i].length 
#  1 <= m, n <= 50 
#  0 <= image[i][j], newColor < 2¹⁶ 
#  0 <= sr < m 
#  0 <= sc < n 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from Queue import Queue
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if newColor == image[sr][sc]: return image
        que, old, = [(sr, sc)], image[sr][sc]
        while que:
            point = que.pop()
            image[point[0]][point[1]] = newColor
            for new_i, new_j in zip((point[0], point[0], point[0] + 1, point[0] - 1),
                                    (point[1] + 1, point[1] - 1, point[1], point[1])):
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == old:
                    que.insert(0, (new_i, new_j))
        return image
        # 起始颜色和目标颜色相同，则直接返回原图
        # if newColor == image[sr][sc]:
        #     return image
        # # 设置四个方向偏移量，一种常见的省事儿技巧
        # directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        # # 构造一个队列，先把起始点放进去
        # que = Queue()
        # que.put((sr, sc))
        # # 记录初始颜色
        # originalcolor = image[sr][sc]
        # # 当队列不为空
        # while not que.empty():
        #     # 取出队列的点并染色
        #     point = que.get()
        #     image[point[0]][point[1]] = newColor
        #     # 遍历四个方向
        #     for direction in directions:
        #         # 新点是(new_i,new_j)
        #         new_i = point[0] + direction[0]
        #         new_j = point[1] + direction[1]
        #         # 如果这个点在定义域内并且它和原来的颜色相同
        #         if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == originalcolor:
        #             que.put((new_i, new_j))
        # return image
# leetcode submit region end(Prohibit modification and deletion)
