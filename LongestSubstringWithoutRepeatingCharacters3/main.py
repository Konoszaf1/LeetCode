# Definition for singly-linked list.
from typing import Optional
import itertools

class Solution:
    # Too slow, iteration over huge strings took too long
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     maximum_length = 0
    #     for index, letter in enumerate(s):
    #         for x in range(len(s), 0, -1):
    #             if x - index < maximum_length:
    #                 continue
    #             if len(set(s[index:x])) == len(s[index:x]) and len(s[index:x]) > maximum_length:
    #                 maximum_length = len(s[index:x])
    #     return maximum_length

    # Cutting down on only unique elements and permutating them is even slower
    # O(n!) for permutations => big no

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     maximum_length = 0
    #     set_string = list(dict.fromkeys(s))
    #     for i in range(len(set_string), 0, -1):
    #         if i < maximum_length:
    #             break
    #         for string in itertools.permutations(set_string, i):
    #             if "".join(string) in s and len(string) >= maximum_length:
    #                 maximum_length = len(string)
    #     return maximum_length\

    # Moving window solution with both window edges mobile
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum_length = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maximum_length = max(maximum_length,right - left + 1)
        return maximum_length


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))