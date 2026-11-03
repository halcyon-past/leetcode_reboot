class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        moves=0
        for i in nums:
            moves += mx-i
        return moves