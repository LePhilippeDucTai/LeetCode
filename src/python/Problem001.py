def two_sum(nums: list[int], target: int) -> list[int]:
    inverse_image = {target - x: i for i, x in enumerate(nums)}
    return next(
        [i, j]
        for i, n in enumerate(nums)
        if (n in inverse_image) and (j := inverse_image.get(n)) != i
    )


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)
