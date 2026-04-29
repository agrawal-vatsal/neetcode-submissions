class Solution:
    valid_dict = {
        '(': ')',
        '{': '}',
        '[':']'
    }

    def isValid(self, s: str) -> bool:
        letter_stack = []
        for ch in s:
            if ch in self.valid_dict:
                letter_stack.append(ch)
                continue

            if len(letter_stack) == 0 or self.valid_dict[letter_stack[-1]] != ch:
                return False
            
            letter_stack.pop()

        return len(letter_stack) == 0

            