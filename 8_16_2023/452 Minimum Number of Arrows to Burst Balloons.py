# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150&fbclid=IwAR064HTE7YBGWsWGU2RqC8SglQIsUAz7aNw2g3hWXX1LA4xfAL06ARumO1Q

# 22:44
# 23:00
# 00:16


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points = sorted(points)

        temp = points[0]
        count = 1
        for i in range(1, len(points)):
            if(temp[1] >= points[i][0]):
                temp[1] = min(temp[1], points[i][1])
            else:
                temp = points[i]
                count += 1
        return count