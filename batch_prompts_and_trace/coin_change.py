from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 3, 4], 6))  # Expected: 2
    print(sol.coinChange([2], 3))        # Expected: -1
    print(sol.coinChange([1], 0))        # Expected: 0
    print(sol.coinChange([1, 2, 5], 11)) # Expected: 3