class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        total = 0
        for i in range(n-1):
            if (s[i]==s[i+1]):
                total +=1
        

        if s[n-1]==s[0]:
            total += 1
        
        if k==total:
            return n-total
        
        if k==total-1:
            return total
        
        return 0