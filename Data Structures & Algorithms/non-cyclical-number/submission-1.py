class Solution:
    def get_next(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        return sum([digit * digit for digit in digits])

    def isHappy(self, n: int) -> bool:
        slow = self.get_next(n)
        fast = self.get_next(self.get_next(n))

        while slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return slow == 1