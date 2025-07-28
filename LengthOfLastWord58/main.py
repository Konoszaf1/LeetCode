class Solution:
    # Solution by Katerina <3
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        letter = ""
        counter = 0
        while (letter != " " or counter == 0) and index >= 0:
            letter = s[index]
            index -= 1
            if letter != " ":
                counter += 1
        return counter

if __name__ == "__main__":
    print(Solution().lengthOfLastWord(" Katerina "))

