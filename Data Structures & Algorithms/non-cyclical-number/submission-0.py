class Solution:
    def calculate_sum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        return sum([digit * digit for digit in digits])

    def isHappy(self, n: int) -> bool:
        nums = set()

        while n not in nums:
            nums.add(n)
            n = self.calculate_sum(n)

            if n == 1:
                return True
        
        return False