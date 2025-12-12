# Compute the n-th Fibonacci number modulo m.
# Naive 
# assume there is an iteration cycle for every input m
# 1. Compute the Fib[i] only before found the length of cycle in the iteration sequence (Fib[i]/m)
# 2. Divide i to the length of cycle and get the remainder, used as index
# 3. Retrieve the index to get the final answer: the n-th Fibonacci number modulo m.
#Problem of Naive Algo: Not scalable!!
#n must be between 0 and 10**6.
# m must be between 2 and 10**3.


# def fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     print(fibonacci_huge_naive(n, m))

# Advance: Pisano Period
# Iteration Logic: 1(rem) + 0 (rem) = 1(rem)
# Necessity : Because there are limited remainder combination, the sequence is forced to hit that 1, 0, 1 combination eventually
# for the index of previous % m , current % m is 1,0 , get the index of previous as the lenght of itt


def get_pissano_period(m):
    previous =0
    current = 1
    for i in range (0, m*m):
        previous, current = current, (previous + current) % m
        if (previous ==0 and current ==1):
            return i+1

def mod_fibo_huge_fast(n,m):
    if not (0<=n<=10**14):
        raise ValueError("Input n must be between 0 and 10**14.")
    if not (2<=m<=10**3):
        raise ValueError("Input m must be between 2 and 10**3.")
    if n <=1:
        return n
    #1. Find the length of repitition cycle
    period = get_pissano_period(m)
    # 2 Reduce input n
    n_reduced = n % period
    # 3 Compute the fib number for the reduced_n, run iteration on the small number 
    if n_reduced <= 1:
        return n_reduced
    previous =0
    current = 1
    for _ in range(n_reduced - 1):
        previous, current = current , (previous + current) % m
    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(mod_fibo_huge_fast(n, m))