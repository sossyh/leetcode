class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands=[]
        
        for i in tokens:
                if i=="+":
                    operand1=operands.pop()
                    operand2=operands.pop()
                    result= operand1 + operand2
                    operands.append(result)
                elif i=="-":
                    operand1=operands.pop()
                    operand2=operands.pop()
                    result= operand2 - operand1
                    operands.append(result)
                elif i=="*":
                    operand1=operands.pop()
                    operand2=operands.pop()
                    result= operand1 * operand2
                    operands.append(result)
                elif i=="/":
                    operand1=operands.pop()
                    operand2=operands.pop()
                    result= operand2 / operand1
                    operands.append(int(result))
                else:
                    operands.append(int(i))
                        
        return operands[0]
            
            