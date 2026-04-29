from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data_map = defaultdict(list)

        for item in strs:
            data_map[frozenset(Counter(item).items())].append(item)

        return data_map.values()