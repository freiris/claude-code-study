from typing import List
import unittest

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_cases(self):
        self.assertEqual(self.solution.coinChange([1, 3, 4], 6), 2)
        self.assertEqual(self.solution.coinChange([2], 3), -1)
        self.assertEqual(self.solution.coinChange([1], 0), 0)
        self.assertEqual(self.solution.coinChange([1, 2, 5], 11), 3)
    
    def test_edge_cases(self):
        self.assertEqual(self.solution.coinChange([1], 1), 1)
        self.assertEqual(self.solution.coinChange([2, 5], 1), -1)
        self.assertEqual(self.solution.coinChange([1, 2, 5], 0), 0)
    
    def test_single_coin_solutions(self):
        self.assertEqual(self.solution.coinChange([5], 10), 2)
        self.assertEqual(self.solution.coinChange([3], 9), 3)
        self.assertEqual(self.solution.coinChange([7], 14), 2)
    
    def test_impossible_amounts(self):
        self.assertEqual(self.solution.coinChange([3, 5], 1), -1)
        self.assertEqual(self.solution.coinChange([2, 4], 3), -1)
    
    def test_large_amounts(self):
        self.assertEqual(self.solution.coinChange([1, 5, 10, 25], 67), 9)

if __name__ == "__main__":
    unittest.main()