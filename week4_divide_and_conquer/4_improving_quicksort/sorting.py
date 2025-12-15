# from random import randint


# def partition3(array, left, right):
#     # write your code here


# def randomized_quick_sort(array, left, right):
#     if left >= right:
#         return
#     k = randint(left, right)
#     array[left], array[k] = array[k], array[left]
#     m1, m2 = partition3(array, left, right)
#     randomized_quick_sort(array, left, m1 - 1)
#     randomized_quick_sort(array, m2 + 1, right)


import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = r
    i = l + 1
    while i <= k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
            i += 1
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1
    return j, k # Returns range of pivots [j, k]

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
