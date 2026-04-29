from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        length = len(s1)

        i = 0
        s2_dict = defaultdict(int)

        while i < length:
            s2_dict[s2[i]] += 1
            i += 1

        if frozenset(c1.items()) == frozenset(s2_dict.items()):
            return True

        while i < len(s2):
            s2_dict[s2[i]] += 1
            s2_dict[s2[i - length]] -= 1
            if s2_dict[s2[i - length]] == 0:
                s2_dict.pop(s2[i - length])

            i += 1
            if frozenset(c1.items()) == frozenset(s2_dict.items()):
                return True

        return False
        