def cat_rep(st, char, times):
    if times == 0:
        return st
    return cat_rep(st + char, char, times - 1)


class Solution:
    def intToRoman2(self, num: int) -> str:
        thousands, hundreds, tens, units = self.split_number(num)
        ret = ""
        ret += self.convert_thousands(thousands)
        ret += self.convert_hundreds(hundreds)
        ret += self.convert_tens(tens)
        ret += self.convert_units(units)
        return ret

    def split_number(self, num: int):
        thousands = int(num / 1000) * 1000
        hundreds = int((num - thousands) / 100) * 100
        tens = int((num - hundreds - thousands) / 10) * 10
        units = num % 10
        return thousands, hundreds, tens, units

    def convert_thousands(self, thousands: int) -> str:
        return cat_rep("", "M", thousands // 1000)

    def convert_hundreds(self, hundreds: int) -> str:
        if hundreds == 400:
            return "CD"
        if hundreds == 500:
            return "D"
        if hundreds == 900:
            return "CM"
        if hundreds > 500:
            return cat_rep("D", "C", (hundreds // 100) - 5)
        return cat_rep("", "C", hundreds // 100)

    def convert_tens(self, tens: int) -> str:
        if tens == 40:
            return "XL"
        if tens == 50:
            return "L"
        if tens == 90:
            return "XC"
        if tens > 50:
            return cat_rep("L", "X", (tens // 10) - 5)
        return cat_rep("", "X", tens // 10)

    def convert_units(self, units: int) -> str:
        if units == 4:
            return "IV"
        if units == 5:
            return "V"
        if units == 9:
            return "IX"
        if units > 5:
            return cat_rep("V", "I", units - 5)
        return cat_rep("", "I", units)

    def intToRoman(self, num):
        d = {
            1000: "M",
            2000: "MM",
            3000: "MMM",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            200: "CC",
            300: "CCC",
            600: "DC",
            700: "DCC",
            800: "DCCC",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            20: "XX",
            30: "XXX",
            60: "LX",
            70: "LXX",
            80: "LXXX",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
            2: "II",
            3: "III",
            6: "VI",
            7: "VII",
            8: "VIII",
            0: "",
        }

        return (
            d[(num // 1000) * 1000]
            + d[((num % 1000) // 100) * 100]
            + d[((num % 100) // 10) * 10]
            + d[(num % 10)]
        )


if __name__ == "__main__":
    s = Solution()
    x = s.intToRoman(58)
    print(x)
