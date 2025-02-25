class Solution:
    def median_of_sorted(self, xs):
        max_pos = len(xs) - 1
        if (max_pos + 1) % 2:  # odd number
            return xs[int((max_pos) / 2)]
        return 0.5 * (xs[int((max_pos - 1) / 2)] + xs[int((max_pos + 1) / 2)])

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def merge(acc: list[int], X, Y):
            if not X and Y:
                acc.extend(Y)
                return acc
            if X and not Y:
                acc.extend(X)
                return acc
            x, *xs = X
            y, *ys = Y
            if x < y:
                acc.append(x)
                return merge(acc, xs, Y)
            acc.append(y)
            return merge(acc, X, ys)

        return self.median_of_sorted(merge([], nums1, nums2))


if __name__ == "__main__":
    S = Solution()
    num1 = [1, 2, 9]
    num2 = [3, 4]
    print(num1 + num2)
    x = S.findMedianSortedArrays(num1, num2)
    print(x)
