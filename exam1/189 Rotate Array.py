class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swap
        n = len(nums)
        k = k % n
        startPoint = 0
        currentPoint = 0
        prevPoint = nums[startPoint]
        iterCount = 0
        while(iterCount < n):
            currentPoint = (currentPoint + k) % n

            temp = nums[currentPoint]
            nums[currentPoint] = prevPoint
            prevPoint = temp
            iterCount += 1
            
            if(currentPoint == startPoint and iterCount < n):
                currentPoint += 1
                startPoint += 1
                prevPoint = nums[startPoint]
            


            

