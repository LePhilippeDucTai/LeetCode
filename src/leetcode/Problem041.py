from typing import List
import functools as ft
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsset = filter((lambda x : x > 0), set(nums))
        first_int = lambda x, y : x + (x >= y)
        return ft.reduce(first_int, numsset, 1)

if __name__ == "__main__":
    S = Solution()
    x = S.firstMissingPositive([0,1,2,-1,1,7,8,9])
    print(x)