class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closetSum = float('inf')
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sumAll = nums[i] + nums[left] + nums[right]
                if sumAll < target:
                    left += 1
                else:
                    right -=1
                if abs(sumAll - target) < abs(closetSum - target):
                    closetSum = sumAll
        return closetSum