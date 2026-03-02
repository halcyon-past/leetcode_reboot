class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr = [0] * n

        for i in range(n):
            streak = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    streak += 1
                else:
                    break
            arr[i] = streak

        steps = 0

        for i in range(n):
            need = n - i - 1

            j = i

            while j < n and arr[j] < need:
                j += 1

            if j == n:
                return -1

            while j > i:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                steps += 1   
                j -= 1       

            steps += j - i
            val = arr.pop(j)
            arr.insert(i, val)

        return steps