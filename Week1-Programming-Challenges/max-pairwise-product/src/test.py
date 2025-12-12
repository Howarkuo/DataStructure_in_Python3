# import random
# import sys
# import os

# test =int(sys.argv[1])
# n=int(sys.argv[2])

# for i in range(test):
#     print ("Test_" + str( i ))
#     os.system("python3 gen.py_"+str(n)+ "_"+str(i)+"_>_input.txt")
#     os.system("python3 model.py_<input.txt_>model.txt")
#     os.system("python3 main.py_<input.txt_>main.txt")
#     with open ('modex.txt') as f: model = f.read()
#     print ("Model:_", model)
#     with open ('main.txt') as f: main = f.read()
#     print ("Main:_", main)
#     if model != main:
#         break


# import random
# import sys
# import os

# tests = int(sys.argv[1])
# n = int(sys.argv[2])

# for i in range(tests):
#     print("Test_" + str(i))

#     # 1. Generate Input: Use spaces, not underscores, and correct redirection
#     # Assuming the generator is named 'gen.py'
#     os.system("poetry run python gen.py " + str(n) + " " + str(i) + " > input.txt")

#     # 2. Run Model Solution: Assuming a separate model file 'model.py'
#     os.system("poetry run python model.py < input.txt > model.txt")

#     # # 3. Run Main Solution: Assuming a separate main file 'main.py'
#     os.system("poetry run python main.py < input.txt > main.txt")

#     # 4. Read Model Output: Use the correct file name 'model.txt'
#     with open('model.txt') as f:
#         model = f.read()
#     print("Model: ", model.strip()) # Use strip() to remove trailing newlines

#     # # 5. Read Main Output: Use the correct file name 'main.txt'
#     with open('main.txt') as f:
#         main = f.read()
#     print("Main: ", main.strip()) # Use strip() to remove trailing newlines

#     # 6. Check the answers
#     if model != main:
#         print("DIFFERENCE FOUND at seed " + str(i) + "!")
#         break



# test.py
import os
import sys

tests = int(sys.argv[1])
n = int(sys.argv[2])
# number of running cases -> test
# number of integers in each test -> n 
# the current running case -> i 
# test.py 2 3  test = 2, n = 3 , i = 0, 1 
#n=int(sys.argv[1]) -> n = 3
#myseed = int(sys.argv[2]) ->  i = 0, 1 
#print(" ".join( [str(random.randint(1,1000)) for i in range(n)])) -> choose n =3 random number
#gen.py output
# =======================
#           3
#       138 583 868 
# #         |
#           v
#        input.txt
#           |
# #         v
#          --------------------
#       |                       |
#       v                       v
# main.py reads             model.py reads
#sys.stdin.read() split          sys.stdin.read() split
# data = [3,138 583 868]   data = [3,138 583 868]
# n = 3                     n = 3
# input_numbers = [138 583 868]
#           |
#           v
# fast_max_pairwise_product / max_pairwise_product
#           |
#           v
# compute 583 * 868 = 506044
#           |
#           v
# output

for i in range(tests):
    print(f"Running Test_{i}")

    # 1. Generate Input
    os.system(f"poetry run python gen.py {n} {i} > input.txt")

    # 2. Run model solution (slow reference)
    os.system("poetry run python model.py < input.txt > model.txt")

    # 3. Run main solution (optimized)
    os.system("poetry run python main.py < input.txt > main.txt")

    # 4. Read outputs
    with open("model.txt") as f:
        model = f.read().strip()

    with open("main.txt") as f:
        main = f.read().strip()

    # 5. Compare
    if model != main:
        print(f"❌ DIFFERENCE FOUND at seed {i}!")
        print(f"Model output: {model}")
        print(f"Main output:  {main}")
        break
    else:
        print(f"✅ Test_{i} passed!\n")

else:
    print("🎉 All tests passed successfully!")