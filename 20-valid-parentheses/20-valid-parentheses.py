class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = { ')': '(', '}': '{', ']': '[' }
        stack = []
        for char in s:
            if char in parentheses.keys():
                if len(stack) == 0 or stack.pop() != parentheses[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0