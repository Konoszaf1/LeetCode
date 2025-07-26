import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s) != None

if __name__ == "__main__":
    print(Solution().isMatch(s="aa", p="a*"))