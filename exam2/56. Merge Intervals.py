class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sortedIntervals = sorted(intervals, key = lambda x:x[0])
        res = [sortedIntervals[0]]
        for current in sortedIntervals[1:]:
            if current[0] <= res[-1][1]:
                res[-1][1] = max(current[1],res[-1][1])
            else:
                res.append(current)
        return res
    
        