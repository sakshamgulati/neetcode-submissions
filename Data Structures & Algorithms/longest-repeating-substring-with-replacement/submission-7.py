class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        charCount = defaultdict(int)
        ans = 0
        fp = 0

        for sp in range(len(s)):
            charCount[s[sp]] += 1  # add current char FIRST

            # shrink window while it's invalid
            while (sp - fp + 1) - max(charCount.values()) > k:
                charCount[s[fp]] -= 1
                fp += 1

            ans = max(ans, sp - fp + 1)  # window LENGTH, not max freq

        return ans