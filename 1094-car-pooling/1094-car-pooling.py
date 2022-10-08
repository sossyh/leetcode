class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passangers , increase = 0, [0] * 1001
        for [n, fro, to] in trips:
            if n> capacity:
                return False
            increase[fro] += n
            increase[to] -= n
        for i in range(1001):  
            passangers  += increase[i]
            if passangers  > capacity: 
                return False  
        return True