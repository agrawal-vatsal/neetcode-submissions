import math
class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self.operations:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.operations[token](x, y))
                continue
            stack.append(int(token))
        return stack[0]
                