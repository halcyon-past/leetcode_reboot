class Solution:
    def maxProduct(self, n: int) -> int:
        l = sorted(list(str(n)))[::-1]
        return int(l[0])*int(l[1])