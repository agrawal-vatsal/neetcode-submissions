class Solution:

    def pop(self, arr: list, idx: int, zero_count: int) -> int:
        arr[idx] -= 1

        if arr[idx] == 0:
            return zero_count + 1
        
        if arr[idx] == -1:
            return zero_count - 1

        return zero_count

    def push(self, arr: list, idx: int, zero_count: int) -> int:
        arr[idx] += 1
        if arr[idx] == 1:
            return zero_count - 1
        
        if arr[idx] == 0:
            return zero_count + 1

        return zero_count

    def get_idx(self, char: str) -> int:
        return ord(char) - ord('a')
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        zero_count = 0
        arr = [0] * 26

        for char in s1:
            idx = self.get_idx(char)
            zero_count = self.pop(arr, idx, zero_count)

        for i in range(len(s2)):
            if i >= len(s1):
                idx = self.get_idx(s2[i - len(s1)])
                zero_count = self.pop(arr, idx, zero_count)

            idx = self.get_idx(s2[i])
            zero_count = self.push(arr, idx, zero_count)
            if zero_count == 0:
                return True

        return False
        