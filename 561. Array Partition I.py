class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        maxsum = 0
        while i < len(nums):
            maxsum += nums[i]
            i += 2
        return maxsum
            
            
            
