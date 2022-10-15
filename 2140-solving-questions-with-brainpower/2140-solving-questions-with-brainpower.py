class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points = [0] * n
        points[n-1] = questions[n-1][0]
        for i in range(n - 2, -1, -1):
            exclude = points[i+1] 
            include = questions[i][0] 
            j = i + questions[i][1] + 1
            if j < n:
                include += points[j]
            points[i] = max(exclude, include)
        return points[0]