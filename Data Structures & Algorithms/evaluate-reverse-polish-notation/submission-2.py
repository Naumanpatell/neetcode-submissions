class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    stack.append(val1+val2)
                elif token == "-":
                    stack.append(val1-val2)
                elif token == "*":
                    stack.append(val1*val2)
                else:
                    stack.append(int(val1 / val2))
        return stack[0]

# Revised today (21 July 2026) --> mixed the val1 and val2 in the stack.pop() and forgot to put the int with the division part.

            
