class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        bracketMap = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
                continue
            if(len(stack) < 1 or stack.pop() != bracketMap[char]):
                return False
        return len(stack) == 0
            