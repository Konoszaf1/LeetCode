from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1]) if x > 0 else -int(str(abs(x))[::-1])
        if result > 2**31 - 1 or result < - 2**31:
            return 0
        return result


if __name__ == "__main__":
    print(Solution().reverse(1234566789123))