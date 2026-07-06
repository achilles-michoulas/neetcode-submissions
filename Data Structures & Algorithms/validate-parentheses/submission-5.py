from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        closeToOpen = {')': '(', 
                       ']': '[', 
                       '}': '{'}
        
        for char in s:
            if stack and char in closeToOpen:
                if stack.pop() != closeToOpen[char]:
                    return False

            elif not stack and char in closeToOpen:
                return False

            else:
                stack.append(char)
        
        return not stack

        
            
