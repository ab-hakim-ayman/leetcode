from typing import List, Dict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            if target-num in index.keys():
                return [index[target-num], idx]
            index[num] = idx
        return []
    
s = Solution()
index = s.twoSum([2,7,9,11], 9)
print(index)