class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if i+k<=len(nums):
                flagFirst = True
                for j in range(k-1):
                    if not(nums[i+j]<nums[i+j+1]):
                        flagFirst=False
                print(i,flagFirst)
                if i+(2*k)<=len(nums):
                    flagSecond = True
                    for j in range(k-1):
                        if not(nums[i+k+j]<nums[i+j+k+1]):
                            flagSecond=False
                    print(flagSecond)
                    if flagFirst and flagSecond:
                        return True
        return False
