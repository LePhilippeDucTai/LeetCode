class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = list()
        if numRows == 1:
            return s
        else :
            n = numRows - 1
            for i, c in enumerate(s) :
                if int(i / n) % 2 == 0:
                    k = i % n 
                else :
                    k = n - i % n  
                l.append((k, c))
            l.sort(key = lambda tup : tup[0])
            y = map(lambda tup : tup[1], l)
            ret = "".join(y)
            return(ret)
        
            


if __name__ == "__main__":
    S = Solution()
    x = S.convert("paypalishiring", 1)
    print(x)
    x2 = S.convert("paypalishiring", 4)
    x3 = S.convert("paypalishiring", 3)
    print(x2)
    print(x3)
