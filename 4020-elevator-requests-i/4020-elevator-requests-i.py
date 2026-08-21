class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        req_len = len(requests)

        total = 0

        for i in range(1,req_len):
            total += abs(requests[i-1]-requests[i])
        
        return total+requests[0]