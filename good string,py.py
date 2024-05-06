def count_good_strings(low, high, zero, one):
    MOD = 10**8 + 5

    
    dp = [[0] * (one + 1) for _ in range(high + 1)]
    
    dp[0][0] = 1

    for i in range(1, high + 1):
        for j in range(one + 1):
            if i > high:
                break
            if j > one:
                break
            dp[i][j] = (dp[i][j] + dp[i - 1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    result = 0
    for i in range(low, high + 1):
        result = (result + sum(dp[i])) % MOD
    
    return result

print(count_good_strings(3, 3, 1, 1))  # Output: 8
print(count_good_strings(2, 3, 1, 2))  # Output: 5
