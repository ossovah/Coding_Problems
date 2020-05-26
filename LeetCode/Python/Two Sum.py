class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for i, n in enumerate(nums):
          cmpl = target - n
          if cmpl not in h:
            h[n] = i
          else:
            return [h[cmpl], i]