# 2-2 
# Naive 


# def fibonacci_last_digit(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10


# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_last_digit(n))

# wrong trial- no need to store all Fibonacci number
# 1. Create array to get Fib(n)
# 2. Update  of the last digit of all Fib[i] only

# def last_digit_fib(n):
#     if not (0<=n<=10**6):
#         raise ValueError("Input n must be between 0 and 10**6.")
#     if n <=1:
#         return n
#     else:
#         fib_last_digits = [0] *(n+1)
#         fib_last_digits[1] =1 
#         # initialize array with index starts from 0,f[0] =0, f[1]=1
#         for i in range(2, n+1):
#             fib_last_digits[i] = (fib_last_digits[i-1]+fib_last_digits[i-2])%10
#         return fib_last_digits[n]
#         # loop n-1 times
#         # Constant operation
# if __name__ == '__main__':
#     input_n = int(input())
#     print(last_digit_fib(input_n))

# Time Complexity:
# O(n)

# 3.Fastest
def fast_last_digit_fib_pisanno(n):
    n_reduced = n %60
    if n_reduced <= 1:
        return n_reduced
    previous, current= 0,1 
    for _ in range (n_reduced-1):
        previous, current = current, (previous+current)%10
    return current

if __name__ == '__main__':
    input_n = int(input())
    print(fast_last_digit_fib_pisanno(input_n))