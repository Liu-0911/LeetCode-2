# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
# 
#  Related Topics 数组 双指针 排序 👍 712 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution():
    def sortedSquares(self, nums: list[int]):
    #
    #     if len(nums) == 1:
    #         return [nums[0] * nums[0]]
    #
    #     # 初始化双指针
    #     left = 0
    #     right = len(nums) - 1
    #
    #     # 存储结果数组，从数组末尾开始存储
    #     res = [-1] * len(nums)
    #     site = len(nums) - 1
    #
    #     # 注意这里是 <=
    #     while left <= right:
    #         # 从两端遍历，将平方数组大得存储在 res 数组中
    #         if nums[left] * nums[left] < nums[right] * nums[right]:
    #             res[site] = nums[right] * nums[right]
    #             right -= 1
    #         else:
    #             res[site] = nums[left] * nums[left]
    #             left += 1
    #
    #         site -= 1
    #
    #     return res
        double = [i ** 2 for  i in nums]
        return double.sort()
# leetcode submit region end(Prohibit modification and deletion)

