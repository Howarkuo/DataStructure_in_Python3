# Recursive: Tree shape
#1. Naive Algorithm:
# F(n), if n<=1, return 1, else return F(n-1)+ F(n-2)
#2. Standard
# def fibonacci_number(n):
#     if n <= 1:
#         return n
#     else:
#       return fibonacci_number(n - 1) + fibonacci_number(n - 2)


#Time Complexity
# O(2^n)-
# always 2 recursive call for each nodes

# Iterative: Line shape, never recalculate , never look back
# 3. Optimized
# Concept: Replacing the recursive function calls with an iterative loop using an array or a couple of variables
#ARRAY!!- Mutable data with same data type
def fibonacci_array(n):
    if not (0<=n<=45):
        raise ValueError("Input n must be between 0 and 45.")
    if n <=1:
        return n
    fib = [0] *(n+1)
    fib[1] =1 
    # initialize array with index starts from 0,f[0] =0, f[1]=1
    for i in range(2, n+1):
        fib[i] = fib[i-1] +fib[i-2]
    return fib[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_array(input_n))
# Time Complexity:
# O(n)
#each Fib(n) is computed once, with n-1 iteration


