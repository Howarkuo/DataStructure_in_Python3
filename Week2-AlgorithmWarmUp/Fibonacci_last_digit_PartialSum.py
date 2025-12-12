#Last Digit of the Partial Sum of Fibonacci
# NumbersProblem

#Naive 

# def fibonacci_partial_sum_naive(n_0, n):
#     _sum = 0

#     current = 0
#     _next  = 1

#     for i in range(n + 1):
#         if i >= n_0:
#             _sum += current

#         current, _next = _next, current + _next

#     return _sum % 10


# if __name__ == '__main__':
#     n_0, n = map(int, input().split())
#     print(fibonacci_partial_sum_naive(n_0, n))


#Faster way:

#1. Goal: Partial Sum = Total Sum(0,n) - Total Sum(0,n_0-1) 
#1.1 Last digit of partial sum: {Total Sum(0,n)- Total Sum(0,n_0)} mod(10)
#2. Period of iteration: 60 ( Pisaon Perioid for mod 10)
#3. Perform Iteration: prev, current = current , (prev+ current) %10

# 3.1 Parital sum: (Fn+2 -1) - (Fn+1 -1 )
# Partial sum: F(n+1) -1 

def fast_fibonacci_last_digit_sum_v2(n):
    if n <= 1:
        return n
    reduced_n = n % 60
    if reduced_n <= 1:
        return reduced_n
    previous , current = 0,1 
    for _ in range(n-1):
        previous , current = current , (previous+ current) %10
    return current
def fast_fibonacci_partial_sum_naive(n_0, n):
    right = fast_fibonacci_last_digit_sum_v2 (n+2)
    #n_0 -1 (+2)    = n_0 +1 
    left = fast_fibonacci_last_digit_sum_v2(n_0+1)

    return (right - left +10) % 10







if __name__ == '__main__':
    n_0, n = map(int, input().split())
    print(fast_fibonacci_partial_sum_naive(n_0, n))