class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        count = []

        for c in s:
            if c in pairs:
                if count and count[-1] == pairs[c]:
                    count.pop()
                else:
                    return False
            else:
                count.append(c)
        return True if not count else False

        