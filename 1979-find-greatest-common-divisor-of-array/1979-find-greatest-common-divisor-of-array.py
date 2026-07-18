class Solution:
    def gcd(self,a,b):
        while (b!=0):
            temp = b
            b = a%b
            a = temp
        return a
    def findGCD(self, nums: List[int]) -> int:
        mx,mn = max(nums),min(nums)
        return self.gcd(mx,mn)
        