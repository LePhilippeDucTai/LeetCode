from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except ValueError:
            return len(nums)


if __name__ == "__main__":
    S = Solution()
    nums = [3, 2, 2, 3]
    x = S.removeElement(nums, 3)
    print(x, nums)
