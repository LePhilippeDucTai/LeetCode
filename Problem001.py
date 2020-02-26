import numpy as np
from typing import List
class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsset = set(nums)
        for ind, val in enumerate(nums):
            if (target - val) in numsset and ind != nums.index(target-val):
                return [ind,nums.index(target-val)]
        return []
