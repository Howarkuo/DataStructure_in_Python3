# def majority_element_naive(elements):
#     for e in elements:
#         if elements.count(e) > len(elements) / 2:
#             return 1

#     return 0

def get_majority_element(a, left, right):
    # Base case
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
        
    mid = (left + right - 1) // 2 + 1
    left_elem = get_majority_element(a, left, mid)
    right_elem = get_majority_element(a, mid, right)
    
    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem: lcount += 1
    if lcount > (right - left) // 2: return left_elem
    
    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem: rcount += 1
    if rcount > (right - left) // 2: return right_elem
    
    return -1
if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
