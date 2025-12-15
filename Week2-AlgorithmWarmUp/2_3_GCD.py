# 2-3 
#Naive 
# compute the greatest common divisor of two positive integers
# 1< GCD < min(a,b)
# GCD: a % d =0, b% = 0 
# def gcd(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd


# if __name__ == "__main__":
#     a, b = map(int, input().split())
#     print(gcd(a, b))
# # O(min (a,b))
  
# Faster
# Reduce dimension of the dimension of remainder to search : Euclidean Division
# GCD(A,B) = GCD(B, A%B)

def gcd_euc(a,b):
    while b:
        a,b = b, a%b
    return a 


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euc(a, b))