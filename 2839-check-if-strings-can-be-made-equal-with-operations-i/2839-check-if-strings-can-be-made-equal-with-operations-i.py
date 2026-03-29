class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a02= s1[0]==s2[2] and s1[2]==s2[0]
        b02= s1[0]==s2[0] and s1[2]==s2[2]
        a13= s1[1]==s2[3] and s1[3]==s2[1]
        b13= s1[1]==s2[1] and s1[3]==s2[3]
        return ((a02 or b02) and (a13 or b13))