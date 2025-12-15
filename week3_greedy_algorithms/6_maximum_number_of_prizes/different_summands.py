def optimal_summands(n):
    summands = []
    current =1 
    # write your code here
    # Greedy step: take 'current' if the remainder is greater than 'current'
    while n > 2 * current:
        summands.append(current)
        n -= current
        current += 1
    summands.append(n)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
