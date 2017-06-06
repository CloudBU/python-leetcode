# ����A��N����ͬ��������ɣ����������[0, N-1]����������
# ����0 <= K <N �� S[K] �������£�
# S[K] = {A[K]��A[A[K]]��A[A[A[K]]]��...}
# ���� S[K] ����ÿ��K�����޵ģ���Ӧ�����ظ��
# дһ��������N��������ɵ�����A�ĺ��������ظ��������󼯺�S[K]�Ĵ�С


"""
��1:

����: A = [5,4,0,3,1,6,2]
���: 4
����: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

���ļ��� S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

"""

# ע��:
# 
# 1. N ����������Χ[1, 20,000].
# 2. A �е�Ԫ�ظ�����ͬ
# 3. A ����������Χ[0, N-1].


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