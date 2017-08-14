# ����һ������n + 1�����������飬����ÿһ������������[1, n]֮�䣬֤������������һ���ظ�Ԫ�ش��ڡ�
# ����ֻ��һ�����ֳ����ظ����ҳ�����ظ������֡�
"""
Note:
 �������޸����飨����������ֻ���ģ�
 ֻ��ʹ�ó����ռ�
 ����ʱ�临�Ӷ�Ӧ��С��O(n2)
 ������ֻ����һ���ظ��������ǿ����ظ����
"""

class Solution(object):
    def findDuplicate(self, nums):
        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = 0
        fast = 0
    
        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
    
            if slow == fast:
                break
    
        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
    
            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow
                
                
"""
second solution:
 ���ַ�
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            cnt = sum(x <= mid for x in nums)
            if cnt > mid:
                high = mid - 1
            else:
                low = mid + 1
        return low