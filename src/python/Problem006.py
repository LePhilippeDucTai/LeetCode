class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        def first(tup):
            return tup[0]

        def second(tup):
            return tup[1]

        n = numRows - 1

        def odd_part(p):
            return int(p / n) % 2

        def up_down(i):
            return n - i % n if odd_part(i) else i % n

        ls = [(up_down(i), c) for i, c in enumerate(s)]
        ls.sort(key=first)
        return "".join(map(second, ls))


if __name__ == "__main__":
    S = Solution()
    x = S.convert("paypalishiring", 1)
    print(x)
    x2 = S.convert("paypalishiring", 4)
    x3 = S.convert("paypalishiring", 5)
    print(x2)
    print(x3)
