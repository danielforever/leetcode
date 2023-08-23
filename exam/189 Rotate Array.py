class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        startPoint = 0
        currentPoint = 0
        prevPoint = nums[startPoint]
        iterCount = 0
        while(iterCount < n):
            currentPoint = (currentPoint + k) % n

            temp = nums[currentPoint]
            nums[currentPoint] = prevPoint
            prevPoint = temp
            
            if(currentPoint == startPoint):
                currentPoint += 1
                startPoint += 1
                prevPoint = nums[startPoint]
            

