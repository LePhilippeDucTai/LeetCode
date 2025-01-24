
def printThis(func) :
    def wrapper(*args, **kwargs):
        s = func(*args, **kwargs)
        print(s)
        return(s)
    return(wrapper)

class Solution:

    @staticmethod
    def isOverflow(x : float) -> bool :
        if (x > 2**31 - 1 or x < -2**31) :
            return True
        else :
            return False

    @printThis
    def reverse(self, x: int) -> int:
        sign = lambda x : -1. if (x < 0) else 1.
        if self.isOverflow(x) :
            return 0
        else :
            r = abs(x)
            xs = list(reversed(str(r)))
            s = sign(x) * float("".join(xs)) 
            if self.isOverflow(s) :
                return 0
            else :
                return int(s)


if __name__ == "__main__":
    s = Solution()
    yy = 1534236469
    print(yy)
    y = s.reverse(yy)
    y1 = s.reverse(-1951511)
        

