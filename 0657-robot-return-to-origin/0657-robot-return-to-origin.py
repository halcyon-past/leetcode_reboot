class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {
            "R": (1,0),
            "L": (-1,0),
            "U":(0,-1),
            "D":(0,1)
        }
        res = [0,0]
        for move in moves:
            res[0] += direction[move][0]
            res[1] += direction[move][1]
        if res==[0,0]:
            return True
        return False