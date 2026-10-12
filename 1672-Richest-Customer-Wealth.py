class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richest = 0

        for arr in accounts:
            total = sum(arr)
            richest = max(richest, total)

        return richest