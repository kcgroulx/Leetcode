class Solution:
    def maxScore(self, s: str) -> int:
        maxValue = 0
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            value = left.count("0") + right.count("1")
            if value > maxValue:
                maxValue = value
        return maxValue