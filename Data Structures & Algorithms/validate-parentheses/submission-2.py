class Solution:
    valid_dict = {
        '(': ')',
        '{': '}',
        '[':']'
    }

    def isValid(self, s: str) -> bool:
        letter_stack = []
        for char in s:
            if char in self.valid_dict:
                letter_stack.append(char)
                continue
            
            if len(letter_stack) == 0:
                return False

            if self.valid_dict[letter_stack[-1]] != char:
                return False

            letter_stack.pop()

        return len(letter_stack) == 0


            