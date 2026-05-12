class Solution:

    def get_unique_dicts(self, dicts: List[dict]) -> List[dict]:
        return [dict(fset) for fset in {frozenset(dictionary.items()) for dictionary in dicts}]


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = [[defaultdict(int)]]

        for i in range(1, target + 1):
            arr.append([])
            for num in nums:
                if i - num < 0:
                    continue

                for item in arr[i - num]:
                    new_dict = defaultdict(int, item)
                    new_dict[num] += 1
                    arr[i].append(new_dict)
                
            arr[i] = self.get_unique_dicts(arr[i])

        ans = []
        for item in arr[target]:
            ans_array = []
            for ans_item in item:
                ans_array.extend([ans_item] * item[ans_item])
            ans.append(ans_array)
        return ans

        