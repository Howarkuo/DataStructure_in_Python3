#Note of Data Structures & Algorithms: Algorithmic Toolbox Part 1 from Daniel M Kane

# Alexander Kulikov

# Pavel Pevzner

# Michael Levin

# Neil Rhodes
#Offered by UNIVERSITY OF CALIFORNIA SAN DIEGO and HSE UNIVERSITY
# reason to learn this course: 
# 1. Although LLM-assisted is powerful, it is important to identify the quality of code
# 2. Beside architecture, it is important to have hand-on experience and personal style on computational problem
# reason for me to write this note:
# 1. Serve as an identification of what I've learned :I don't have time for physical course attendance instead I took this course on coursera  
# 2. Serve as my repository for answer for different algorithm questions



# Maximum Pairwise Product
#  max ai * aj
# 1. Naive Algorithm
# 2. Fast Algorithm


#1.1 
# MaxPairWiseProductNaive (A[1...n]):
# (1) product = 0
# (2)for i from 1 to n:
# (3)  for j from i+1 to n:
# (4)     product = max(product A[i]* A[j])
# (5) return Product

# 1.2 Time Complextity Order: N^2 /2 -> O (N^2)

#(1): 1
#(2): N
#(3): Summation of N-i (i=1, N-1) = ( N^2 - N )/ 2 (inner loop run)
#(4): 3 * Inner loop run times
#(5): 1 

#1.3 Define package used
# -Python - max() function: return the largest value within an iterable 
#input(): take in user input -> turn string into int
#map (type, target): returns a iterator-list for input 

#1.4 model.py 
import sys
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0 
    for first in range(n):
        for second in range(first+1, n):
            max_product = max(max_product, numbers[first]*numbers[second])
    return max_product


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    input_numbers = data[1:]
    print(max_pairwise_product(input_numbers))

# 1.5 Test my solution
# Generate test 
#int(sys.argv[1]): Take in the first value input after the script in command line
#random.seed(): Reproducable random number generator

# 1.6 Faster Function
# MaxPairWiseProductFast (A[1...n]):
# (1) index1 =1 
# (2)for i from 2 to n:
# (3)if A[i] > A[index]:
# (4)   index1= i
# (5) if index1 ==0:
#       index2 = 1
#     else:
#        idex2 =0  
# (6) for j from 1 to n:
# (7) if A[j] ≠ A[index1] and A[j] > A[index2]
#     index2 = j
#  return A [index1] * A[index2]


# 1.7 workflow 
# (1) use gen.py to generate reproducible inputs
# (2) use main.py / model.py to run algorithm on that input
# (3) use stress_test.py to check correctness automatically