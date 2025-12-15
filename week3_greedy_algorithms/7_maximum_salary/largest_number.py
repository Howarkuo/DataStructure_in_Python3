# from itertools import permutations


# def largest_number_naive(numbers):
#     numbers = list(map(str, numbers))

#     largest = 0

#     for permutation in permutations(numbers):
#         largest = max(largest, int("".join(permutation)))

#     return largest


# if __name__ == '__main__':
#     _ = int(input())
#     input_numbers = input().split()
#     print(largest_number_naive(input_numbers))

from functools import cmp_to_key
import sys

def largest_number(a):
    # Custom comparator
    # Returns 1 if x should come before y
    # Returns -1 if y should come before x
    # Returns 0 if they are equal
    def compare(x, y):
        if x + y > y + x:
            return -1 # x comes first (in Python sort, -1 puts it earlier)
        elif x + y < y + x:
            return 1  # y comes first
        else:
            return 0

    # Convert all integers to strings
    a = list(map(str, a))
    
    # Sort using the custom logic
    a.sort(key=cmp_to_key(compare))
    
    # Join them
    return "".join(a)

if __name__ == '__main__':
    # Using sys.stdin for potentially faster I/O in Python
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
        
    n = input_data[0]
    input_numbers = input_data[1:]