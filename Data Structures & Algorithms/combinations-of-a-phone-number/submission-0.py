class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        num_to_char_map = {
            "3": ["d", "e", "f"],
            "2": ["a", "b", "c"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []

        ans = []
        for char in digits:
            if len(ans) == 0:
                ans = num_to_char_map[char]
                continue
            new_ans = []
            for item in ans:
                for num_char in num_to_char_map[char]:
                    new_ans.append("".join([item, num_char]))
            ans = new_ans

        return ans
