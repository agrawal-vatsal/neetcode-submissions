class Solution:

    def pop(self, arr: list, idx: int, x: int) -> int:
        arr[idx] -= 1

        if arr[idx] == 0:
            return x + 1
        
        if arr[idx] == -1:
            return x - 1

        return x

    def push(self, arr: list, idx: int, x: int) -> int:
        arr[idx] += 1
        if arr[idx] == 1:
            return x - 1
        
        if arr[idx] == 0:
            return x + 1

        return x

    def get_idx(self, char: str) -> int:
        return ord(char) - ord('a')
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = 26
        arr = [0] * 26

        for char in s1:
            idx = self.get_idx(char)
            x = self.pop(arr, idx, x)

        for i in range(len(s2)):
            if i >= len(s1):
                idx = self.get_idx(s2[i - len(s1)])
                x = self.pop(arr, idx, x)

            idx = self.get_idx(s2[i])
            x = self.push(arr, idx, x)
            if x == 26:
                return True

        return False
        