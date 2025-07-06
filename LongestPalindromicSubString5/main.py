class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for index, letter in enumerate(s):
            left = index
            right = index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(max_palindrome):
                    max_palindrome = s[left:right + 1]
                left -= 1
                right += 1
            left = index
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(max_palindrome):
                    max_palindrome = s[left:right + 1]
                left -= 1
                right += 1

        return max_palindrome

if __name__ == "__main__":
    print(Solution().longestPalindrome("aacabdkacaa"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("aaaa"))
    print(Solution().longestPalindrome("abcba"))