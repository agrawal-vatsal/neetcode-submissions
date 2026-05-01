from collections import defaultdict
class Solution:
    def pop(self, char: str, data_map: defaultdict, missing_chars: int, build: bool = False) -> int:
        if build == False:
            if char not in data_map:
                return missing_chars

        data_map[char] -= 1
        if data_map[char] == -1:
            return missing_chars + 1

        return missing_chars

    def push(self, char: str, data_map: defaultdict, missing_chars: int) -> int:
        if char not in data_map:
            return missing_chars

        data_map[char] += 1
        if data_map[char] == 0:
            return missing_chars - 1
        return missing_chars

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_length = math.inf
        missing_chars = 0
        ans = tuple()
        data_map = defaultdict(int)

        for char in t:
            missing_chars = self.pop(char, data_map, missing_chars, build=True)

        l = r = 0
        while True:
            if r == len(s):
                break

            while missing_chars > 0:
                if r == len(s):
                    return ""

                char = s[r]
                missing_chars = self.push(char, data_map, missing_chars)
                r += 1

            while missing_chars == 0:
                curr_length = r - l + 1
                if min_length > curr_length:
                    min_length = curr_length
                    ans = (l, r + 1)

                char = s[l]
                missing_chars = self.pop(char, data_map, missing_chars)
                l += 1

        if ans == ():
            return ""

        return s[ans[0]: ans[1]]

        