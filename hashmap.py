from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, i in enumerate(nums):
            complement = target - i
            if complement in hasher:
                return [hasher[complement], idx]
            hasher[i] = idx