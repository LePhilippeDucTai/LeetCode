from typing import List
import functools as ft
class Solution:
    def maxArea(self, height: List[int]) -> int:
        def loop(i, j, acc) :
            distance = j - i
            if distance :
                if height[i] < height[j] :
                    return loop(i + 1, j, max(acc, distance * height[i]))
                else :
                    return loop(i, j - 1, max(acc, distance * height[j]))
            else :
                return acc
        return loop(0, len(height) - 1, 0)

    def maxArea2(self, height: List[int]) -> int:
        maximum = -1
        i, j = 0, len(height) - 1
        while i < j :
            if height[i] < height[j] :
                maximum = max(maximum, (j - i) * height[i])
                i += 1
            else :
                maximum = max(maximum, (j-i) * height[j])
                j -= 1
        return maximum

if __name__ == "__main__":
    s = Solution()
    heights = [1,8,6,2,5,4,8,3,7]
    couples = enumerate(heights)
    r = s.maxArea(heights)
    print(r)