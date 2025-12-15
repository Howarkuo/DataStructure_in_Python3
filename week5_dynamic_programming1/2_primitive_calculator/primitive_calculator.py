# def compute_operations(n):
#     return []


# if __name__ == '__main__':
#     input_n = int(input())
#     output_sequence = compute_operations(input_n)
#     print(len(output_sequence) - 1)
#     print(*output_sequence)

def optimal_sequence(n):
    sequence = []
    ops = [0] * (n + 1)
    
    for i in range(2, n + 1):
        min_ops = ops[i-1] + 1
        if i % 2 == 0:
            min_ops = min(min_ops, ops[i//2] + 1)
        if i % 3 == 0:
            min_ops = min(min_ops, ops[i//3] + 1)
        ops[i] = min_ops

    # Backtrack
    curr = n
    while curr > 1:
        sequence.append(curr)
        if curr % 3 == 0 and ops[curr//3] == ops[curr] - 1:
            curr //= 3
        elif curr % 2 == 0 and ops[curr//2] == ops[curr] - 1:
            curr //= 2
        else:
            curr -= 1
    sequence.append(1)
    return reversed(sequence)