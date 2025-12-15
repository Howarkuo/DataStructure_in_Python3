from itertools import combinations


# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions


# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     print(inversions_naive(elements))


def merge_and_count(a, b, left, mid, right):
    i, j, k = left, mid, left
    inv_count = 0
    while i < mid and j < right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            inv_count += (mid - i) # Important step
        k += 1
    # Copy remaining
    while i < mid:
        b[k] = a[i]
        i += 1; k += 1
    while j < right:
        b[k] = a[j]
        j += 1; k += 1
    for i in range(left, right):
        a[i] = b[i]
    return inv_count

def get_number_of_inversions(a, b, left, right):
    inv_count = 0
    if right - left <= 1:
        return inv_count
    mid = (left + right) // 2
    inv_count += get_number_of_inversions(a, b, left, mid)
    inv_count += get_number_of_inversions(a, b, mid, right)
    inv_count += merge_and_count(a, b, left, mid, right)
    return inv_count