from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            if hasher.get(i) is None:
                return [hasher.get(i), idx]
            hasher[i] = idx