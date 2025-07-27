class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        string = ""
        thousanths = num // 1000
        remainder = num % 1000
        if thousanths > 0:
            string += "M" * thousanths
        if remainder > 100 and str(remainder).startswith("4"):
            string += "CD"
        elif remainder > 100 and str(remainder).startswith("9"):
            string += "CM"
        else:
            hundreds = remainder // 100
            string += "C" * hundreds if hundreds < 4 else "D" + "C" * (hundreds - 5)

        remainder %= 100
        tenths = remainder // 10
        if tenths > 0 and str(tenths).startswith("4"):
            string += "XL"
        elif tenths > 0 and str(tenths).startswith("9"):
            string += "XC"
        else:
            string += "X" * tenths if tenths < 4 else "L" + "X" * (tenths - 5)

        remainder %= 10
        if str(remainder).startswith("4"):
            string += "IV"
        elif str(remainder).startswith("9"):
            string += "IX"
        else:
            digits = remainder
            string += "I" * digits if digits < 4 else "V" + "I" * (digits - 5)
        return string

if __name__ == "__main__":
    print(Solution().intToRoman(3749))
    print(Solution().intToRoman(44))
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(4))
    print(Solution().intToRoman(900))
    print(Solution().intToRoman(400))