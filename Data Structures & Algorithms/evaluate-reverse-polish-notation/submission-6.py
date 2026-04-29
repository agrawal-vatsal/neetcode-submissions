import math
class Solution:
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)
    }

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for char in tokens:
            if char in self.operations:
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                num_stack.append(self.operations[char](num1, num2))
            else:
                num_stack.append(int(char))

            print(num_stack)

        return num_stack[0]
                