# #Naive
# def fibonacci_sum_squares(n):
#     if n <= 1:
#         return n

#     previous, current, sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10


# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_sum_squares(n))


## Modify so it only store and update the sum % 10 in the loop enough, not in the final step
## Is it faster to initiate a 
#Faster 

# def fast_fibonacci_sum_squares(n):
#     if n <= 1:
#         return n

#     previous, current, sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, (previous + current) %10
#         #Keep it small!
#         sum = (sum+ current * current) %10
#         # Keep it small!

#     return sum % 10


# if __name__ == '__main__':
#     n = int(input())
#     print(fast_fibonacci_sum_squares(n))

#Fastest 
#Pisano Period

 
def fibonacci_sum_squares_fastest(n):
    previous =0
    current = 1
    if n <=1:
        return n
    # The Pisano period for modulo 10 is 60 
    reduced_n = n %60 
    if reduced_n <=0 :
        return reduced_n 
    for i in range (reduced_n -1):
        previous, current = current, (previous + current) % 10
    # current is now f_n
    # previous 
    f_n = current
    f_n_plus_one = (previous + current) % 10

    return (f_n * f_n_plus_one) % 10

if __name__ =="__main__":
    n= int(input())
    print(fibonacci_sum_squares_fastest(n))

