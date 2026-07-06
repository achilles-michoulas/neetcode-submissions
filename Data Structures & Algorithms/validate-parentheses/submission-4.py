from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False

        for char in s:
            if stack:
                if char == ')':
                    if stack.pop() != '(':
                        return False 
                elif char == ']': 
                    if stack.pop() != '[':
                        return False
                elif char == '}':
                    if stack.pop() != '{':
                        return False
                else:
                    stack.append(char)
            else:
                if char == ')' or char == '}' or char == '}':
                    return False
                else:
                    stack.append(char)
        
        return not stack

        
            
