from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for item in strs:
            data[frozenset(item)].append(item)

        return list(data.values())