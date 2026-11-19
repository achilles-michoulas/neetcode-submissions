from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = ['+', '-', '/', '*']

        for token in tokens:
            
            if token in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                
                if token == '+':
                    ans = a + b
                elif token == '-':
                    ans = b - a
                elif token == '*':
                    ans = a * b
                elif token == '/':
                    ans = int(b / a)
                    
                
            else:
                ans = int(token)
            
            stack.append(ans)
        
        return stack.pop()
            