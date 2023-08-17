# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/?envType=study-plan-v2&envId=dynamic-programming
# 10:21
# 10:35
# 10:14

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        maxSubsequence = 1
        dp = {}
        for i in range( len(arr)):
            count = 1
            if(arr[i] - difference) in dp:
                count += dp[arr[i] - difference]
                maxSubsequence = max(maxSubsequence, count)
            dp[arr[i]] = count

        return maxSubsequence

            