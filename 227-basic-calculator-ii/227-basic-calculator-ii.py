class Solution:
    def calculate(self, s: str) -> int:
        if len(s)==0:
            return 0
        answer = 0
        prevNum = 0
        currNum = 0
        operator = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if operator == '+' or operator == '-':
                    answer += prevNum
                    prevNum = (currNum if operator == '+' else -currNum)
                elif operator == '*':
                    prevNum *= currNum
                elif operator == '/':
                     prevNum = int(prevNum / currNum)
                operator = c
                currNum = 0
                
        return answer + prevNum