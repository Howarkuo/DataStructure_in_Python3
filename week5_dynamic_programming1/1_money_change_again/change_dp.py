# def change(money):
#     # write your code here

#     return money
def get_change_dp(m):
    # Denominations: 1, 3, 4
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        dp[i] = dp[i-1] + 1
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + 1)
        if i >= 4:
            dp[i] = min(dp[i], dp[i-4] + 1)
    return dp[m]

if __name__ == '__main__':
    m = int(input())
    print(get_change_dp(m))
