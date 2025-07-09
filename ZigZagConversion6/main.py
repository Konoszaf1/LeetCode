from typing import Optional

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_column_index = 0
        next_column_index = (2 * numRows) - 2
        dict1 = {}
        column = -1
        for index, letter in enumerate(s):
            if index == 0 or index % next_column_index == 0:
                column += 1
                new_column_index = new_column_index + next_column_index if index != 0 else 0
            if index in range(new_column_index, new_column_index + numRows):
                dict1[column] = dict1[column] + letter if column in dict1.keys() else letter
            else:
                column += 1
                dict1[column] = letter

        string = ""
        for row in range(numRows):
            for column in dict1.keys():
                if column % (numRows - 1) == 0:
                    if len(string) < len(s):
                        if row < len(dict1[column]):
                            string += dict1[column][row]
                elif row == numRows - column % (numRows - 1) - 1:
                    # 1 = 2 % 3
                    # 3 = 4 %
                    string += dict1[column]
        return string
# for every row the index of the first column is (numberofrows * 2) - 2
# 2 -> 2
# 3 -> 4
# 4 -> 6
# 5 -> 8
# Column should be filled if multiple of new_column_index+3

# Dict approach was too slow, should revisit to improve
if __name__ == "__main__":
    print(Solution().convert("A", 1))