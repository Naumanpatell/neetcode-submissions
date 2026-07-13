class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracs = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in bracs.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != bracs[char]:
                    return False
                stack.pop()
        return len(stack) == 0
