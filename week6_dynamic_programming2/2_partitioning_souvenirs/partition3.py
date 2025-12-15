# from sys import stdin


# def partition3(values):
#     return 0


# if __name__ == '__main__':
#     input_n, *input_values = list(map(int, stdin.read().split()))
#     assert input_n == len(input_values)
#     print(partition3(input_values))


def partition3(A):
    total = sum(A)
    if total % 3 != 0:
        return 0
    target = total // 3
    n = len(A)
    # dp[i][j] = can we fill first partition to i and second to j?
    # Optimization: using dictionary/recursion with memoization is easier 
    # than 3D array for large inputs.
    
    memo = {}

    def search(used_mask, current_sum, count_completed):
        if count_completed == 2: return True # If 2 are full, 3rd is auto full
        state = (used_mask, current_sum)
        if state in memo: return memo[state]
        
        if current_sum == target:
            res = search(used_mask, 0, count_completed + 1)
            memo[state] = res
            return res
        
        for i in range(n):
            if not (used_mask & (1 << i)): # If item i not used
                if current_sum + A[i] <= target:
                    if search(used_mask | (1 << i), current_sum + A[i], count_completed):
                        return True
        
        memo[state] = False
        return False

    return 1 if search(0, 0, 0) else 0