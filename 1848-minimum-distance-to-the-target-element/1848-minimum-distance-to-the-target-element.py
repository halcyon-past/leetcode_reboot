class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        mindist = float('inf')
        for i,j in enumerate(nums):
            ab = abs(i-start)
            if j==target:
                mindist=min(mindist,ab)
        return mindist