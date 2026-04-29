class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        digits[0] += 1

        for i in range(len(digits)):
            if digits[i] >= 10:
                curr_num = digits[i]
                digits[i] %= 10
                if i < len(digits) - 1:
                    digits[i + 1] += curr_num // 10
                else:
                    digits.append(curr_num // 10)

            print(digits)

        return digits[::-1]
