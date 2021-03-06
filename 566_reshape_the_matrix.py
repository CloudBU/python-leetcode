# 在Matlab中有一个非常有用的函数叫 reshape，他可以将矩阵重新组成一个不同的大小，但是不改变其原始数据
# 给出一个由二维数组表示的矩阵，两个正整数r和c分别表示所需重组矩阵的行号和列号。
# 重新组合的矩阵需要以与它们相同的行遍历顺序填充原始矩阵的所有元素。
# 如果具有给定参数的“重塑”操作是可行且合法的，则输出新的重构矩阵; 否则，输出原始矩阵。
"""
例1:

输入:  nums = [[1,2],
               [3,4]]
       r = 1, 
	   c = 4

输出: [[1,2,3,4]]

解释: 数字的行遍历是[1,2,3,4]。 新的重构矩阵是一个1 * 4矩阵，使用上一个列表逐行填充。
"""

"""
例1:

输入:  nums = [[1,2],
               [3,4]]
       r = 2, 
	   c = 4

输出: [[1,2],
       [3,4]]

解释: 无法重塑，输出原来的数组
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        origin_r = len(nums)
        origin_c=len(nums[0])
        if origin_c*origin_r==r*c:
            temp=[num for row in nums for num in row]
            newMatrix=[[0 for j in xrange(c)] for i in xrange(r)]
            for i in xrange(r):
                for j in xrange(c):
                    newMatrix[i][j]=temp[i*c+j]
            return newMatrix
        else:
            return nums