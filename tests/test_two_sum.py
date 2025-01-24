import pytest

from leetcode.problems.two_sum import two_sum

baselines = [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])]


@pytest.mark.parametrize("nums,target,expected", baselines)
def test_two_sum_01(nums, target, expected):
    assert two_sum(nums, target) == expected
