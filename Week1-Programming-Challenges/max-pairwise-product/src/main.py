# import sys
# def fast_max_pairwise_product(numbers):
#     n = len(numbers)
#     # Find the largest number
#     max1_index = 0
#     for i in range(1, n):
#         if numbers[i] > numbers[max1_index]:
#             max1_index = i

#     # Find the second largest number (different index)
#     max2_index = -1
#     for i in range(n):
#         if i != max1_index and (max2_index == -1 or numbers[i] > numbers[max2_index]):
#             max2_index = i

#     return numbers[max1_index] * numbers[max2_index]


# if __name__ == '__main__':
#     data = list(map(int, sys.stdin.read().split()))
#     n = data[0]
#     input_numbers = data[1:]
#     print(fast_max_pairwise_product(input_numbers))


import sys
def fast_max_pairwise_product(numbers):
    n = len(numbers)
    # Find the largest number
    max1_index = 0
    for i in range(1, n):
        if numbers[i] > numbers[max1_index]:
            max1_index = i

    if max1_index == 0:
        max2_index =1
    else:
        max2_index=0
    # Find the second largest number (different index)
    for j in range(1, n):
        if j != max1_index: 
            if numbers[j] > numbers[max2_index]:
                max2_index = j

    return numbers[max1_index] * numbers[max2_index]


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    input_numbers = data[1:]
    print(fast_max_pairwise_product(input_numbers))
# 138 583 868 

#[stdin stream]  "3 138 583 868"
#       |
#       v
# [sys.stdin.read()]  -> "3 138 583 868"
#       |
#       v
# [list(map(int, ..))] -> [3, 138, 583, 868]
#       |
#       v
# n = data[0]  -> 3
# input_numbers = data[1:] -> [138, 583, 868]
#       |
#       v
# call fast_max_pairwise_product([138,583,868])
#       |
#       v
# +--------------------------+
# | fast_max_pairwise_product|
# +--------------------------+
# | find index of max1 (loop)|
# | init max2_index          |
# | find index of max2 (loop)|
# | return numbers[max1]*numbers[max2]
# +--------------------------+
#       |
#       v
# print(result) -> "506044"


# #Trace with numbers:

# Start: max1_index = 0 → currently largest is numbers[0] = 138.

# i = 1: compare numbers[1] = 583 with numbers[0] = 138. Since 583 > 138, set max1_index = 1. Now largest is 583.

# i = 2: compare numbers[2] = 868 with numbers[1] = 583. Since 868 > 583, set max1_index = 2. Now largest is 868.

# After loop: max1_index == 2 (value 868).

# Initialize second-largest index (max2_index)

# if max1_index == 0:
#     max2_index = 1
# else:
#     max2_index = 0


# Since max1_index is 2 (not 0), max2_index gets 0. So initially second-largest candidate is numbers[0] = 138.

# Find the second-largest (different index):

# for j in range(1, n):
#     if j != max1_index and numbers[j] > numbers[max2_index]:
#         max2_index = j


# Trace:

# j = 1: j != max1_index? yes (1 != 2). Compare numbers[1] = 583 with numbers[0] = 138. Since 583 > 138, set max2_index = 1. Now second-largest candidate = 583.

# j = 2: j != max1_index? no (2 == 2), skip.

# After loop: max2_index == 1 (value 583).