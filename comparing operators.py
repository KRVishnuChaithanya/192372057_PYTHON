def isMatch(s: str, p: str) -> bool:
    # Initialize a DP table to store the results of subproblems
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns with '*' at the beginning
    for j in range(2, len(p) + 1):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
    
    # Populate the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
    
    return dp[len(s)][len(p)]

# Test cases
test_cases = [("aa", "a"), ("aa", "a*"), ("ab", ".*"), ("aaa", "aa"), ("aab", "c*a*b")]
for i, (s, p) in enumerate(test_cases, start=1):
    print("Test Case", i, ":")
    print("Input: s =", s, ", p =", p)
    print("Output:", isMatch(s, p))
    print()
