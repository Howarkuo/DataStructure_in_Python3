from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    items = []
    for i in range(len(weights)):
        if weights[i] != 0:
            items.append((values[i] / weights[i], weights[i], values[i]))
    
    # Sort by ratio descending
    items.sort(key=lambda x: x[0], reverse=True)
    
    for ratio, weight, val in items:
        if capacity == 0:
            return value
        # Take as much as possible
        amount = min(weight, capacity)
        value += amount * ratio
        capacity -= amount

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
