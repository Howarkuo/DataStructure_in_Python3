# def edit_distance(first_string, second_string):
#     return 0


# if __name__ == "__main__":
#     print(edit_distance(input(), input()))


def edit_distance(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1): dp[i][0] = i
    for j in range(m + 1): dp[0][j] = j
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s[i-1] == t[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1,      # Deletion
                           dp[i][j-1] + 1,      # Insertion
                           dp[i-1][j-1] + cost) # Match/Mismatch
    return dp[n][m]