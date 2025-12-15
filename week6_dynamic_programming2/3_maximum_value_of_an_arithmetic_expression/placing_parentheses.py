# def evaluate(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     else:
#         assert False


def maximum_value(dataset):
    # write your code here
    op = []
    nums = []
    import re
    # Simple parsing assuming single digit numbers for brevity, 
    # but re.split is better for multi-digit
    parts = re.split(r'(\D)', dataset)
    nums = [int(x) for x in parts[::2]]
    op = parts[1::2]
    
    n = len(nums)
    min_vals = [[0]*n for _ in range(n)]
    max_vals = [[0]*n for _ in range(n)]

    for i in range(n):
        min_vals[i][i] = nums[i]
        max_vals[i][i] = nums[i]

    def evalt(a, b, op):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b

    def min_and_max(i, j):
        min_v = float('inf')
        max_v = float('-inf')
        for k in range(i, j):
            # Split expression at operator k
            a = evalt(max_vals[i][k], max_vals[k+1][j], op[k])
            b = evalt(max_vals[i][k], min_vals[k+1][j], op[k])
            c = evalt(min_vals[i][k], max_vals[k+1][j], op[k])
            d = evalt(min_vals[i][k], min_vals[k+1][j], op[k])
            min_v = min(min_v, a, b, c, d)
            max_v = max(max_v, a, b, c, d)
        return min_v, max_v

    for s in range(1, n): # s is length of range
        for i in range(n - s):
            j = i + s
            min_vals[i][j], max_vals[i][j] = min_and_max(i, j)
            
    return max_vals[0][n-1]
    # return 0


if __name__ == "__main__":
    print(maximum_value(input()))
