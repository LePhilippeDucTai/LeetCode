from typing import List
class Solution:
    def area(self, u,v):
        x1, y1 = u
        x2, y2 = v
        return abs(x1-x2) * min(y1,y2)

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maximum = -1
        for i in range(n):
            for j in range(i + 1, n):
                maximum = max(maximum, (j - i)*min(height[i], height[j]))
        return maximum


if __name__ == "__main__":
    s = Solution()
    heights = [1,8,6,2,5,4,8,3,7]
    r = s.maxArea(heights)
    print(r)
    