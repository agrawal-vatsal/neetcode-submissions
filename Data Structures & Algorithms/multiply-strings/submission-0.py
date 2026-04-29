class Solution:

    def get_int_from_num(self, num):
        num_int = 0
        for char in num:
            num_int *= 10
            char_num = ord(char) - ord('0')
            num_int += char_num

        return num_int

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        num1_int = self.get_int_from_num(num1)
        num2_int = self.get_int_from_num(num2)

        return str(num1_int * num2_int)