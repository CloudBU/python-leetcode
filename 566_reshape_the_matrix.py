# ��Matlab����һ���ǳ����õĺ����� reshape�������Խ������������һ����ͬ�Ĵ�С�����ǲ��ı���ԭʼ����
# ����һ���ɶ�ά�����ʾ�ľ�������������r��c�ֱ��ʾ�������������кź��кš�
# ������ϵľ�����Ҫ����������ͬ���б���˳�����ԭʼ���������Ԫ�ء�
# ������и��������ġ����ܡ������ǿ����ҺϷ��ģ�������µ��ع�����; �������ԭʼ����
"""
��1:

����:  nums = [[1,2],
               [3,4]]
       r = 1, 
	   c = 4

���: [[1,2,3,4]]

����: ���ֵ��б�����[1,2,3,4]�� �µ��ع�������һ��1 * 4����ʹ����һ���б�������䡣
"""

"""
��1:

����:  nums = [[1,2],
               [3,4]]
       r = 2, 
	   c = 4

���: [[1,2],
       [3,4]]

����: �޷����ܣ����ԭ��������
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