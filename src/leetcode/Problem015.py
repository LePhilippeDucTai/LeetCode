"""
    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
    Given an array nums of n integers, are there elements a, b, c in nums
    such that a + b + c = 0 ?
    Find all unique triplets in the array which gives the sum of zero.

"""

import itertools as it


def two_sum(nums: list[int], target: int) -> list[int]:
    inverse_image = {target - x: i for i, x in enumerate(nums)}
    return next(
        (
            [i, j]
            for i, n in enumerate(nums)
            if (n in inverse_image) and (j := inverse_image.get(n)) != i
        ),
        [],
    )


def filter_results(enum: tuple[int, list[int, int] | None]) -> bool:
    i, val = enum
    if val:
        j, k = val
        return all(x != y for x, y in it.combinations([i, j, k], 2))
    return False


def to_tuple(enum: tuple[int, list[int, int]]) -> tuple[int, int, int]:
    i, (j, k) = enum
    return tuple(sorted([i, j, k]))


class Solution:
    """
    Returns indices such that the sum of two elements of
    nums is equal to target.
    """

    def threeSum(self, nums: list[int]) -> list[tuple[int]]:
        t = (two_sum(nums, -v) for v in nums)
        f = filter(filter_results, enumerate(t))
        s = map(to_tuple, f)
        values = {tuple(sorted(nums[i] for i in v)) for v in s}
        return list(values)


if __name__ == "__main__":
    S = Solution()
    y = S.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    print(y)
