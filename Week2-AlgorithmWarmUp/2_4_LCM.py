#2-4
# #Naive 
# def lcm(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     assert False

# if __name__ == '__main__':
#     a, b = map(int, input().split())
#     print(lcm(a, b))

# # O(a*b)

#Faster 


def gcd_euc(a,b):
    while b:
        a,b = b, a%b
    return a 


def lcm_fast(a,b):
    if a ==0 or b==0:
        return 0
    else:
        return (a*b)// gcd_euc(a,b)
if __name__ =='__main__':
    a, b =map(int, input().split())
    print(lcm_fast(a,b))

