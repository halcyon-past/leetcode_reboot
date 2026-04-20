class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        index, result = inf,0
        for i,c in enumerate(colors):
            if (c!=colors[0]):
                result = i
                index = min(index,i)
            else:
                result = max(result,i-index)
        return result