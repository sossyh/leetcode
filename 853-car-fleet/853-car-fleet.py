class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=list()
        cars = sorted(zip(position,speed))
        time = [(target - c[0])/float(c[1]) for c in cars]
                
        for i in time[::-1]:
            if stack and i <= stack[-1]:
                continue
                
            stack.append(i)
            
        return len(stack)