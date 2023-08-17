# 23:01
# 23:28
# 00:27

#hint: 2D DP 

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        count = 0
        maxSubsequence = 2
        dp = [{} for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                different = nums[i] - nums[j]
                dp[i][different] = dp[j].get(different, 1) + 1
                maxSubsequence = max(maxSubsequence, dp[i][different])

        return maxSubsequence