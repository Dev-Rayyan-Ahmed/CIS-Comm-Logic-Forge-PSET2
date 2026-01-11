def count_payment_combinations(coins, total_sum):
    
    dp = [0] * (total_sum + 1)
    dp[0] = 1  

    for coin in coins:
        for j in range(coin, total_sum + 1):
            dp[j] += dp[j - coin]

    return dp[total_sum]


print()
print("Case A:", count_payment_combinations([1, 2, 3], 4))  # Output: 4
print("Case B:", count_payment_combinations([2, 5, 3, 6], 10))  # Output: 5
print("Case C:", count_payment_combinations([4], 5))  # Output: 0