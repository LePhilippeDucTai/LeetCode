def cat_rep(st, char, times) :
    if times == 0 :
        return st
    else :
        return cat_rep(st + char, char, times - 1)

class Solution:

    def intToRoman2(self, num: int) -> str:
        thousands = int(num / 1000) * 1000
        hundreds = int((num - thousands) / 100) * 100
        tens = int((num - hundreds - thousands)/ 10) * 10
        units = num % 10
        print(thousands, hundreds, tens, units)

        x1 = thousands / 1000
        x2 = hundreds / 100
        x3 = tens / 10
        x4 = units

        ret = ""
        if thousands > 0 :
            ret = cat_rep(ret, 'M', x1)
    
        if 100 <= hundreds and hundreds <= 400 :
            if hundreds == 400 :
                ret = ret + "CD"
            else :
                ret = cat_rep(ret,'C', x2)
        elif hundreds > 400 :
            if hundreds == 500 :
                ret = ret + "D"
            elif hundreds == 900 :
                ret = ret + "CM"
            else :
                ret = cat_rep(ret + "D", 'C', x2 - 5)

        if 10 <= tens and tens <= 40 :
            if tens == 40 :
                ret = ret + "XL"
            else :
                ret = cat_rep(ret, 'X', x3)
        elif tens > 40 :
            if tens == 50 :
                ret = ret + "L"
            elif tens == 90 :
                ret = ret + "XC"
            else :
                ret = cat_rep(ret + "L", 'X', x3 - 5)

        if 1 <= units <= 4 :
            if units == 4 :
                ret = ret + 'IV'
            else :
                ret = cat_rep(ret, 'I', units)
        elif units > 4 :
            if units == 5 :
                ret = ret + "V"
            elif units == 9 :
                ret = ret + "IX"
            else :
                ret = cat_rep(ret + "V", 'I', units - 5)

        return ret

    def intToRoman(self, num):
        d = {1000: "M", 2000 : "MM", 3000 : "MMM",
            900: "CM", 500: "D", 400: "CD", 100: "C", 200: "CC", 300: "CCC", 600: "DC", 700: "DCC", 800: "DCCC",
            90: "XC", 50: "L", 40: "XL", 10: "X", 20: "XX", 30: "XXX",  60: "LX", 70: "LXX", 80: "LXXX",
            9: "IX", 5: "V", 4: "IV", 1: "I", 2: "II", 3: "III", 6: "VI", 7: "VII", 8: "VIII",  0: ""}
            
        return d[(num // 1000) * 1000] + d[((num % 1000)//100)*100] + d[((num % 100)//10)*10] + d[(num % 10)]

if __name__ == "__main__":
    s = Solution()
    x = s.intToRoman(58)
    print(x)