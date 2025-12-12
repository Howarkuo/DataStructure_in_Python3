# Naive 
# 1. Create array to get Fib(n)
# 2. Update  of the last digit of all Fib[i] only

# Standard
def last_digit_fib(n):
    if not (0<=n<=10**6):
        raise ValueError("Input n must be between 0 and 10**6.")
    if n <=1:
        return n
    else:
        fib_last_digits = [0] *(n+1)
        fib_last_digits[1] =1 
        # initialize array with index starts from 0,f[0] =0, f[1]=1
        for i in range(2, n+1):
            fib_last_digits[i] = (fib_last_digits[i-1]+fib_last_digits[i-2])%10
        return fib_last_digits[n]
if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_fib(input_n))

# Time Complexity:
# O(n)