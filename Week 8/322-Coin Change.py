class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')

        dp = [0] + [MAX] * amount
      
        for coin in coins: 
            for current_amount in range(coin, amount + 1):
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
      
        return -1 if dp[amount] == MAX else dp[amount]
        