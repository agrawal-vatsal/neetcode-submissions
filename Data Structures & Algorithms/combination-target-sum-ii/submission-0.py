import copy

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = [set() for _ in range(target + 1)]
        for candidate in candidates:
            if candidate > target:
                continue
            new_arr = copy.deepcopy(arr)
            new_arr[candidate].add((candidate, ))
            for i in range(target - candidate, 0, -1):
                possible_ways = arr[i]
                for way in possible_ways:
                    new_tuple = way + (candidate, )
                    new_arr[i + candidate].add(new_tuple)
            arr = new_arr

        return [list(x) for x in arr[target]]
