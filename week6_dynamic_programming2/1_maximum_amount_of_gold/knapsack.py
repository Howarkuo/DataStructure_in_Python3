# from sys import stdin


# def maximum_gold(capacity, weights):
#     assert False


# if __name__ == '__main__':
#     input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
#     assert len(input_weights) == n

#     print(maximum_gold(input_capacity, input_weights))


def optimal_weight(W, w):
    # w is list of item weights
    # dp[w] will be the max weight we can fit into capacity w
    n = len(w)
    # 2D Array: dp[i][j] = max weight using first i items with capacity j
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i-1][j] # Don't include item i
            if w[i-1] <= j:
                val = dp[i-1][j - w[i-1]] + w[i-1]
                if val > dp[i][j]:
                    dp[i][j] = val
    return dp[n][W]