def two_sum(nums: list[int], target: int) -> list[int]:
    hashtable = {target - x: i for i, x in enumerate(nums)}
    results = (
        [i, j]
        for i, n in enumerate(nums)
        if (n in hashtable) and (j := hashtable.get(n)) != i
    )
    return next(results)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)
