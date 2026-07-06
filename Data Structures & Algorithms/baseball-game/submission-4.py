class Solution:
    def calPoints(self, operations: List[str]) -> int:
        from collections import deque

        stack = deque()

        for operation in operations:
            if operation == 'C':
                if stack:
                    stack.pop()
            elif operation == '+':
                length = len(stack)
                stack.append(stack[length - 1] + stack[length - 2])
            elif operation == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(operation))
        
        sum = 0

        while stack:
            sum += stack.pop()

        return sum
