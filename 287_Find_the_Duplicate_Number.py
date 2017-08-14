# 给定一个包含n + 1个整数的数组，其中每一个整数均介于[1, n]之间，证明其中至少有一个重复元素存在。
# 假设只有一个数字出现重复，找出这个重复的数字。
"""
Note:
 不可以修改数组（假设数组是只读的）
 只能使用常数空间
 运行时间复杂度应该小于O(n2)
 数组中只存在一个重复数，但是可能重复多次
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
 二分法
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