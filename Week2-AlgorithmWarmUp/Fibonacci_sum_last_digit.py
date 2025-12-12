#LastDigitoftheSumofFibonacciNumbers
# Input: An integer n.
# Output: The last digit of F0+F1+· ·· +Fn.
# Naive 
# def fibonacci_last_digit_sum(n):
#     if n <= 1:
#         return n

#     previous, current, _sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         _sum += current

#     return _sum % 10


# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_sum(n))


#Faster 
# If we can get F(n+2) , we can get sum F(n) 
# IF we can get F(n+2) mod (10), we can get LastDigitoftheSumofFibonacciNumbers

def fast_fibonacci_last_digit_sum(n):
    if n <= 1:
        return n
    if not (0<=n<=10**14):
        raise ValueError("Input n must be between 0 and 10**14.")
    #1. Reduced input n dimension
    # (F(n+2) - 1) modulo (10) repeats every 60 numbers
    reduced_n = (n+2 ) % 60
    # 2. Iteration: Calculate F(reduced_n)
    if reduced_n <=1:
        return reduced_n
    else:
        previous, current, = 0, 1

        for _ in range(0, reduced_n -1):
            previous, current = current, (previous + current) %10
        fib_val = current
    # Apply the sum identity: Sum = F(n+2) -1
    if fib_val ==0:
        #special case: if F(n+2) = 0, sum of last digit must not be -1
        # eg. : F15 = 610 , the sum of of last digit will be 10 - 1 = 9
        return 9
    else:
        return fib_val -1


    

if __name__ == '__main__':
    n = int(input())
    print(fast_fibonacci_last_digit_sum(n))