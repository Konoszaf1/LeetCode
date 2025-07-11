class Solution:
    # Open brackets must be closed.
    # Closed in the correct order
    def isValid(self, s: str) -> bool:
        track_open = []
        for char in s:
            if char == "(":
                track_open.append(char)
            elif char == "[":
                track_open.append(char)
            elif char == "{":
                track_open.append(char)
            elif char == ")":
                if len(track_open) == 0 or track_open.pop() != "(":
                    return False
            elif char == "]":
                if len(track_open) == 0 or track_open.pop() != "[":
                    return False
            elif char == "}":
                if len(track_open) == 0 or track_open.pop() != "{":
                    return False
        if len(track_open) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    print(Solution().isValid("]([])"))