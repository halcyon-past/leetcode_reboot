class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = n
        rev = 0
        while m>0:
            rem = m%10
            rev = rev*10+rem
            m = m//10
        print(rev)
        return abs(n-rev)