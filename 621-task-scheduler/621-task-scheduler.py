class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer=0
        m=len(tasks)
        counts=Counter(tasks)
        frequency=[]
        for key in counts:
            frequency.append(counts[key])
        max_frequency=max(frequency)
        max_task=frequency.count(max_frequency)
        result=((max_frequency-1)* (n+1)) + max_task 
        answer=max(m,result)
            
        
        return answer