# Assignment 1 - Sum of 2 digits
# 
# # Define two variables for function
#Approach 1-List comprehension
# 0. input function to accept input - input()
# 1. List comprehension to create list of existing sequence
# 
# 2.Taka input as string and split - input().split(0)
#  
def Addition(first_digit, second_digit):
    return first_digit+second_digit
if __name__ == '__main__':
    a,b = [int(x) for x in input().split() ]
    print(Addition(a,b))

#Approach 2- map function 
# accept string input and turn into integer

def Addition(first_digit, second_digit):
    return first_digit+second_digit
if __name__ == '__main__':
    a,b = map(int, input().split())
    print(Addition(a,b))
