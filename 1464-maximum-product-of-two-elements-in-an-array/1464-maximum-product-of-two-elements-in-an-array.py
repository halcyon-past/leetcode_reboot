class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return ((s := sorted(nums, reverse=True))[0] - 1) * (s[1] - 1)