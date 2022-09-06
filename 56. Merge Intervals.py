
# O(nlogn) Time | O(n) Space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key= lambda x:x[0])
        currentinterval = intervals[0]
        result.append(currentinterval)
        for interval in intervals[1:]:
            currentbegin= currentinterval[0]
            currentend = currentinterval[1]
            nextbegin = interval[0]
            nextend = interval[1]
            if currentend >= nextbegin:
                currentinterval[1] = max(currentend,nextend)
            else:
                currentinterval = interval
                result.append(currentinterval)
            
        
                    
        return result
        
        
