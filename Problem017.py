from typing import List
  
dictionary = {'1' : "", '2' : "abc", '3' : "def", '4' : "ghi", \
    '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}

class Solution:

    def joinDigit(self, li, digit) :
        if li :
            res = []
            for xs in li :
                for b in dictionary[digit]:
                    res.append("".join([xs, b]))
            return res
        else :
            return list(dictionary[digit])

    def letterCombinations(self, digits: str) -> List[str]:
        def loop(acc, dig):
            if dig :
                x, *xs = dig
                if x == '1' :
                    return loop(acc, xs)
                else :
                    return(loop(self.joinDigit(acc, x), xs))
            else :
                return acc
        return loop([], digits)



if __name__ == "__main__":
    S = Solution()
    res = S.letterCombinations("72432")
    print(res)