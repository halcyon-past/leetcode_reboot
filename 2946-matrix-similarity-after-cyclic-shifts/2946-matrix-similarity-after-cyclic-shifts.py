class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        new_mat = mat[:]
        for shift in range(k):
            for i in range(len(new_mat)):
                if i%2==0:
                    new_mat[i] = new_mat[i][1:] + [new_mat[i][0]]
                else:
                    new_mat[i]= [new_mat[i][len(new_mat[i])-1]]+new_mat[i][:len(new_mat[i])-1]
        if mat==new_mat:
            return True
        return False
