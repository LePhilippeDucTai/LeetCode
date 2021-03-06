class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        else :
            first = lambda tup : tup[0]
            second = lambda tup : tup[1]
            n = numRows - 1
            odd_part = lambda p : int( p / n ) % 2 
            up_down = lambda i : n - i % n if odd_part(i) else i % n
            ls = [(up_down(i), c) for i, c in enumerate(s)]
            ls.sort(key = first)
            return "".join(map(second, ls))


if __name__ == "__main__":
    S = Solution()
    x = S.convert("paypalishiring", 1)
    print(x)
    x2 = S.convert("paypalishiring", 4)
    x3 = S.convert("paypalishiring", 5)
    print(x2)
    print(x3)
