def find_longest_mirror_length(s):
    n = len(s)
    if n == 0:
        return 0
        
    # Creating a table to store results of subproblems
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # strings of length 1 are always palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
        
    # building table, cl is length of substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                
    return dp[0][n - 1]

# Driver Code
test_cases = ["bbabcbcab", "cbbd", "racecar"]
print()
for s in test_cases:
    print(f"Input: '{s}'")
    print(f"Result: {find_longest_mirror_length(s)}")
    print("-" * 20)