# 数组A由N个不同的整数组成，该数组包含[0, N-1]的所有整数
# 设置0 <= K <N 的 S[K] 定义如下：
# S[K] = {A[K]，A[A[K]]，A[A[A[K]]]，...}
# 集合 S[K] 对于每个K是有限的，不应包含重复项。
# 写一个给定由N个整数组成的数组A的函数，返回该数组的最大集合S[K]的大小


"""
例1:

输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

最大的集合 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

"""

# 注意:
# 
# 1. N 是整数，范围[1, 20,000].
# 2. A 中的元素各不相同
# 3. A 是整数，范围[0, N-1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return false;
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i