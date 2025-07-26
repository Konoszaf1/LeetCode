from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0
        s = s.strip(" ")
        sign = 1 if s[0] == "+" or s[0].isdigit() else -1
        string = ""
        for index, char in enumerate(s):
            if index == 0 and (char == "+" or char == "-"):
                continue
            elif char.isdigit():
                string += char
            else:
                break
        num = sign * int("".join(string)) if string != "" else 0
        if num >= 2**31 - 1:
            return 2**31 - 1
        elif num <= -2**31:
            return -2**31
        else:
            return num

if __name__ == "__main__":
    print(Solution().myAtoi(""))